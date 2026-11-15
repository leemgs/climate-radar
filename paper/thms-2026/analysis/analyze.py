#!/usr/bin/env python3
"""Re-analysis of the THMS user study from the anonymized raw logs in ../data/.

Run:  python3 -I analyze.py      (writes results.json and results.md next to this file)

Inputs (../data):
  01_participant_info.csv   52 participants
  02_survey_scores.csv      52 x 2 conditions (NASA-TLX, trust, SUS)
  03_trial_logs.csv         52 x 2 x 10 = 1,040 trials

All tests are two-sided. Seeds are fixed. Nothing here is imputed or simulated except
the percentile bootstrap used for the CI of d_z (10,000 resamples, seed 20261115).
"""
from __future__ import annotations
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.power import TTestPower

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
RNG = np.random.default_rng(20261115)
OUT: dict = {}

part = pd.read_csv(DATA / "01_participant_info.csv", encoding="utf-8-sig", keep_default_na=False)
sv = pd.read_csv(DATA / "02_survey_scores.csv")
tr = pd.read_csv(DATA / "03_trial_logs.csv")
tr["ok"] = (tr.selected_action == tr.correct_action).astype(int)
tr["esc"] = (tr.escalation == "Yes").astype(int)
tr["defer"] = (tr.deferral == "Yes").astype(int)

# ---------------------------------------------------------------- data integrity
chk = {}
chk["n_participants"] = int(part.participant.nunique())
chk["n_trials"] = int(len(tr))
chk["trials_per_participant_condition"] = sorted(tr.groupby(["participant", "condition"]).size().unique().tolist())
chk["missing_values"] = int(tr.isna().sum().sum() + sv.isna().sum().sum())
sus_items = [f"SUS_{i}" for i in range(1, 11)]
odd = sv[sus_items[0::2]].sub(1).sum(axis=1)                       # items 1,3,5,7,9
even = (5 - sv[sus_items[1::2]]).sum(axis=1)                       # items 2,4,6,8,10
chk["sus_recomputed_max_abs_diff"] = float(((odd + even) * 2.5 - sv.SUS_overall).abs().max())
sub = ["mental_demand", "physical_demand", "temporal_demand", "performance", "effort", "frustration"]
chk["tlx_mean_of_6_max_abs_diff"] = float((sv[sub].mean(axis=1) - sv.NASA_TLX_overall).abs().max())
tri = ["trust_reliability", "trust_predictability", "trust_appropriateness"]
chk["trust_mean_of_3_max_abs_diff"] = float((sv[tri].mean(axis=1) - sv.trust_overall).abs().max())
# the order recorded in the participant file agrees with the trial log
ord_log = tr[tr.condition == "AI"].groupby("participant").condition_order.first().map({"1st": "AI_First", "2nd": "Baseline_First"})
chk["order_consistent_between_files"] = bool((ord_log.reindex(part.participant).values == part.condition_order.values).all())
OUT["integrity"] = chk

# ---------------------------------------------------------------- demographics
OUT["demographics"] = {
    "age_mean": round(part.age.mean(), 1), "age_sd": round(part.age.std(), 1),
    "age_min": int(part.age.min()), "age_max": int(part.age.max()),
    "gender": part.gender.value_counts().to_dict(),
    "tech_background": part.tech_background.value_counts().to_dict(),
    "disaster_experience": part.disaster_experience.value_counts().to_dict(),
    "condition_order": part.condition_order.value_counts().to_dict(),
}

# ---------------------------------------------------------------- participant-level frame
g = tr.groupby(["participant", "condition"])
pl = g.agg(AER=("ok", "mean"), RT=("response_time_sec", "mean"), RT_med=("response_time_sec", "median"),
           deferral=("defer", "mean")).reset_index()
pl = pl.merge(sv, on=["participant", "condition"]).merge(part[["participant", "condition_order"]]
                                                          .rename(columns={"condition_order": "seq"}), on="participant")


def wide(col):
    w = pl.pivot(index="participant", columns="condition", values=col)
    return w["Baseline"].values, w["AI"].values


def cohen_dz_boot(d):
    n = len(d)
    idx = RNG.integers(0, n, (10000, n))
    bs = d[idx].mean(1) / d[idx].std(1, ddof=1)
    return np.percentile(bs, [2.5, 97.5])


def paired(col, label=None):
    b, a = wide(col)
    d = a - b
    n = len(d)
    t, p = stats.ttest_rel(a, b)
    se = d.std(ddof=1) / np.sqrt(n)
    tcrit = stats.t.ppf(0.975, n - 1)
    dz = d.mean() / d.std(ddof=1)
    J = 1 - 3 / (4 * (n - 1) - 1)
    try:
        w = stats.wilcoxon(a, b, zero_method="wilcox", method="auto")
        wp, wstat = float(w.pvalue), float(w.statistic)
    except ValueError:
        wp, wstat = float("nan"), float("nan")
    sh = stats.shapiro(d)
    lo, hi = cohen_dz_boot(d)
    return {
        "outcome": label or col, "n": n,
        "base_mean": b.mean(), "base_sd": b.std(ddof=1), "ai_mean": a.mean(), "ai_sd": a.std(ddof=1),
        "diff": d.mean(), "diff_sd": d.std(ddof=1), "ci_lo": d.mean() - tcrit * se, "ci_hi": d.mean() + tcrit * se,
        "t": t, "df": n - 1, "p": p, "dz": dz, "dz_ci_lo": lo, "dz_ci_hi": hi, "g_z": dz * J,
        "d_av": d.mean() / ((a.std(ddof=1) + b.std(ddof=1)) / 2),
        "r_within": float(np.corrcoef(a, b)[0, 1]),
        "wilcoxon_W": wstat, "wilcoxon_p": wp, "shapiro_W": float(sh.statistic), "shapiro_p": float(sh.pvalue),
    }


primary = [paired("AER", "AER")]
secondary = [paired("RT", "Response latency (s)"), paired("NASA_TLX_overall", "NASA-TLX overall"),
             paired("trust_overall", "Trust overall"), paired("SUS_overall", "SUS")]
# Holm correction within the secondary family (H2-H4: four tests)
adj = multipletests([r["p"] for r in secondary], method="holm")[1]
adjw = multipletests([r["wilcoxon_p"] for r in secondary], method="holm")[1]
for r, a, aw in zip(secondary, adj, adjw):
    r["p_holm"], r["wilcoxon_p_holm"] = a, aw
primary[0]["p_holm"] = primary[0]["p"]
primary[0]["wilcoxon_p_holm"] = primary[0]["wilcoxon_p"]

expl = [paired(c, c) for c in ["mental_demand", "physical_demand", "temporal_demand", "performance", "effort", "frustration",
                               "trust_reliability", "trust_predictability", "trust_appropriateness"]]
adj = multipletests([r["p"] for r in expl], method="holm")[1]
adjw = multipletests([r["wilcoxon_p"] for r in expl], method="holm")[1]
for r, a, aw in zip(expl, adj, adjw):
    r["p_holm"], r["wilcoxon_p_holm"] = a, aw
# SUS rescored from the ten items with the standard formula (robustness check; see integrity block)
pl["SUS_rescored"] = ((pl[sus_items[0::2]].sub(1).sum(axis=1)) + (5 - pl[sus_items[1::2]]).sum(axis=1)) * 2.5
sus_re = paired("SUS_rescored", "SUS rescored from items")
OUT["primary"], OUT["secondary"], OUT["subscales"] = primary, secondary, expl
OUT["sus_rescored"] = sus_re
OUT["sus_offset_logged_minus_rescored"] = {"min": float((sv.SUS_overall - ((sv[sus_items[0::2]].sub(1).sum(axis=1)) + (5 - sv[sus_items[1::2]]).sum(axis=1)) * 2.5).min()),
                                           "max": float((sv.SUS_overall - ((sv[sus_items[0::2]].sub(1).sum(axis=1)) + (5 - sv[sus_items[1::2]]).sum(axis=1)) * 2.5).max())}

# ---------------------------------------------------------------- sensitivity analyses for the primary outcome
sens = {}
# (a) trial-level logistic GEE, clustered by participant
tr["ai"] = (tr.condition == "AI").astype(int)
gee = smf.gee("ok ~ ai", "participant", data=tr, family=sm.families.Binomial(),
              cov_struct=sm.cov_struct.Exchangeable()).fit()
ci = gee.conf_int().loc["ai"]
sens["aer_gee_logit"] = {"OR": float(np.exp(gee.params["ai"])), "ci_lo": float(np.exp(ci[0])), "ci_hi": float(np.exp(ci[1])),
                         "z": float(gee.tvalues["ai"]), "p": float(gee.pvalues["ai"])}
# (b) latency: linear mixed model on log RT with participant random intercept
tr["logrt"] = np.log(tr.response_time_sec)
lm = smf.mixedlm("logrt ~ ai", tr, groups=tr["participant"]).fit(reml=True)
c = lm.conf_int().loc["ai"]
sens["rt_lmm_log"] = {"ratio": float(np.exp(lm.params["ai"])), "ci_lo": float(np.exp(c[0])), "ci_hi": float(np.exp(c[1])),
                      "z": float(lm.tvalues["ai"]), "p": float(lm.pvalues["ai"])}
# (c) latency distribution (trial level)
q = tr.groupby("condition").response_time_sec.describe(percentiles=[.25, .5, .75, .9]).round(2)
sens["rt_trial_distribution"] = q.to_dict("index")
sens["rt_max"] = float(tr.response_time_sec.max())
# (d) correctness vs. timeliness: AER as logged = correct-action rate. What if a response-time cutoff T also had to be met?
cut = {}
for T in (10, 12, 15, 20):
    for cond in ("Baseline", "AI"):
        d = tr[tr.condition == cond]
        cut.setdefault(str(T), {})[cond] = {
            "late_share": float((d.response_time_sec > T).mean()),
            "aer_correct_and_in_time": float(((d.ok == 1) & (d.response_time_sec <= T)).mean())}
    d_ = tr.assign(hit=((tr.ok == 1) & (tr.response_time_sec <= T)).astype(int)).groupby(["participant", "condition"]).hit.mean().unstack()
    tt = stats.ttest_rel(d_["AI"], d_["Baseline"])
    cut[str(T)]["paired_t"] = float(tt.statistic); cut[str(T)]["paired_p"] = float(tt.pvalue)
    cut[str(T)]["diff"] = float((d_["AI"] - d_["Baseline"]).mean())
sens["time_cutoff_sensitivity"] = cut
# (e) failure structure: every trial that is not a success is a wrong-action trial in the logs
sens["failures"] = {cond: {"wrong_action_trials": int((d.ok == 0).sum()), "n": int(len(d))} for cond, d in tr.groupby("condition")}
# (f) RT of correct vs wrong trials
sens["rt_by_correctness"] = tr.groupby(["condition", "ok"]).response_time_sec.mean().round(2).unstack().to_dict("index")
# (g) correct-action distribution by condition (difficulty / composition control)
ct = pd.crosstab(tr.condition, tr.correct_action)
chi = stats.chi2_contingency(ct)
sens["correct_action_by_condition"] = {"table": ct.to_dict("index"), "chi2": float(chi[0]), "dof": int(chi[2]), "p": float(chi[1])}
# (h) is the correct action tied to a scenario label?
w = tr.pivot_table(index=["participant", "scenario"], columns="condition", values="correct_action", aggfunc="first")
sens["same_correct_action_baseline_vs_ai_for_same_slot"] = float((w.AI == w.Baseline).mean())
sens["n_distinct_correct_actions_per_slot_label"] = int(tr.groupby("scenario").correct_action.nunique().min())
# (i) per-slot AER
sens["aer_by_slot"] = tr.groupby(["scenario", "condition"]).ok.mean().round(3).unstack().to_dict("index")
OUT["sensitivity"] = sens

# ---------------------------------------------------------------- order / carry-over (2x2 crossover logic)
order = {}
for col in ["AER", "RT", "NASA_TLX_overall", "trust_overall", "SUS_overall"]:
    w_ = pl.pivot(index="participant", columns="condition", values=col)
    seq = part.set_index("participant").condition_order.reindex(w_.index)
    d = (w_["AI"] - w_["Baseline"])
    s = (w_["AI"] + w_["Baseline"])
    a_, b_ = d[seq == "AI_First"], d[seq == "Baseline_First"]
    t1 = stats.ttest_ind(a_, b_, equal_var=False)
    sa, sb = s[seq == "AI_First"], s[seq == "Baseline_First"]
    t2 = stats.ttest_ind(sa, sb, equal_var=False)
    order[col] = {"diff_AI_first": float(a_.mean()), "diff_Base_first": float(b_.mean()),
                  "order_x_condition_t": float(t1.statistic), "order_x_condition_p": float(t1.pvalue),
                  "carryover_t": float(t2.statistic), "carryover_p": float(t2.pvalue)}
# same logic on trial scale: second-period vs first-period AER and latency irrespective of condition
per = tr.groupby(["participant", "condition_order"]).agg(AER=("ok", "mean"), RT=("response_time_sec", "mean")).unstack()
order["period_effect_AER_2nd_minus_1st"] = float((per["AER"]["2nd"] - per["AER"]["1st"]).mean())
order["period_effect_RT_2nd_minus_1st"] = float((per["RT"]["2nd"] - per["RT"]["1st"]).mean())
OUT["order_effects"] = order

# ---------------------------------------------------------------- escalation / deferral (descriptive)
ai = tr[tr.condition == "AI"]
base = tr[tr.condition == "Baseline"]
esc = {"n_ai_trials": int(len(ai)), "n_escalated": int(ai.esc.sum()), "share_escalated": float(ai.esc.mean())}
esc["participants_with_any_escalation"] = int((ai.groupby("participant").esc.sum() > 0).sum())
esc["escalated_per_participant_min_med_max"] = [int(x) for x in ai.groupby("participant").esc.sum().agg(["min", "median", "max"])]
for name, d in [("baseline_all", base), ("ai_all", ai), ("ai_not_escalated", ai[ai.esc == 0]), ("ai_escalated", ai[ai.esc == 1])]:
    esc[name] = {"n": int(len(d)), "AER": float(d.ok.mean()), "deferral": float(d.defer.mean()),
                 "RT": float(d.response_time_sec.mean()), "RT_sd": float(d.response_time_sec.std())}
# deferral rate: paired comparison at participant level
b, a = wide("deferral")
dd = a - b
t, p = stats.ttest_rel(a, b)
tcrit = stats.t.ppf(.975, len(dd) - 1)
esc["deferral_paired"] = {"base": float(b.mean()), "ai": float(a.mean()), "diff": float(dd.mean()),
                          "ci": [float(dd.mean() - tcrit * dd.std(ddof=1) / np.sqrt(len(dd))), float(dd.mean() + tcrit * dd.std(ddof=1) / np.sqrt(len(dd)))],
                          "t": float(t), "p": float(p), "dz": float(dd.mean() / dd.std(ddof=1))}
# within AI: escalation vs deferral (chi-square on trials; descriptive, clustered data)
ctab = pd.crosstab(ai.esc, ai.defer)
chi = stats.chi2_contingency(ctab, correction=False)
esc["ai_escalation_x_deferral"] = {"table": ctab.to_dict("index"), "chi2": float(chi[0]), "p": float(chi[1])}
esc["deferral_and_correct_ai"] = {"deferred_AER": float(ai[ai.defer == 1].ok.mean()), "not_deferred_AER": float(ai[ai.defer == 0].ok.mean())}
OUT["escalation"] = esc

# ---------------------------------------------------------------- scale reliability (Cronbach alpha)
def alpha(df):
    k = df.shape[1]
    return float(k / (k - 1) * (1 - df.var(ddof=1).sum() / df.sum(axis=1).var(ddof=1)))


sv2 = sv.copy()
for i in (2, 4, 6, 8, 10):
    sv2[f"SUS_{i}"] = 6 - sv2[f"SUS_{i}"]
rel = {}
for cond in ("Baseline", "AI"):
    s_ = sv2[sv2.condition == cond]
    rel[cond] = {"trust_3items": alpha(s_[tri]), "SUS_10items": alpha(s_[sus_items]), "TLX_6subscales": alpha(s_[sub])}
OUT["reliability"] = rel

# ---------------------------------------------------------------- power
pw = TTestPower()
OUT["power"] = {"n": 52, "alpha": 0.05, "power": 0.80,
                "min_detectable_dz": float(pw.solve_power(effect_size=None, nobs=52, alpha=0.05, power=0.80)),
                "observed_dz_AER": primary[0]["dz"]}


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    return o


OUT = clean(OUT)
(HERE / "results.json").write_text(json.dumps(OUT, indent=2, ensure_ascii=False))

# compact markdown summary
L = ["# Re-analysis summary (generated by analyze.py)", ""]
L.append("| Outcome | Base M (SD) | AI M (SD) | Diff [95% CI] | t(51) | p | p_Holm | d_z [95% CI] | Wilcoxon p |")
L.append("|---|---|---|---|---|---|---|---|---|")
for r in OUT["primary"] + OUT["secondary"] + OUT["subscales"]:
    L.append(f"| {r['outcome']} | {r['base_mean']:.3f} ({r['base_sd']:.3f}) | {r['ai_mean']:.3f} ({r['ai_sd']:.3f}) | "
             f"{r['diff']:.3f} [{r['ci_lo']:.3f}, {r['ci_hi']:.3f}] | {r['t']:.2f} | {r['p']:.2e} | {r['p_holm']:.2e} | "
             f"{r['dz']:.2f} [{r['dz_ci_lo']:.2f}, {r['dz_ci_hi']:.2f}] | {r['wilcoxon_p']:.2e} |")
(HERE / "results.md").write_text("\n".join(L) + "\n")
print(json.dumps(OUT, indent=1, ensure_ascii=False))
