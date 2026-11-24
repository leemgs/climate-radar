#!/usr/bin/env python3
"""Robustness analyses added for the second round of review (2026-11-24).

They address concerns that the records cannot settle directly (scenario identity and difficulty across
conditions, carry-over, dependence on the scoring key) by checking whether the primary conclusions hold
under analyses that need only the logged fields. Nothing here changes any reported number.

Run:  python3 -I robustness.py     (writes robustness.json and robustness.md next to this file)
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

HERE = Path(__file__).resolve().parent
d = pd.read_csv(HERE.parent / "data" / "03_trial_logs.csv")
d["ok"] = (d.selected_action == d.correct_action).astype(int)
d["ai"] = (d.condition == "AI").astype(int)
d["first"] = (d.condition_order == "1st").astype(int)
rng = np.random.default_rng(20261124)
R = {}

# participant-level AER and latency
pl = d.groupby(["participant", "condition"]).agg(aer=("ok", "mean"), rt=("response_time_sec", "mean")).unstack()
diff = pl["aer"]["AI"] - pl["aer"]["Baseline"]

# (1) First period only: each participant contributes one condition, so there is no carry-over and no
#     reuse of scenarios across conditions (between-subjects comparison, 28 AI-first vs 24 Baseline-first).
f = d[d.first == 1].groupby(["participant", "condition"]).agg(aer=("ok", "mean"), rt=("response_time_sec", "mean")).reset_index()
a, b = f[f.condition == "AI"], f[f.condition == "Baseline"]
def welch(x, y):
    t, p = stats.ttest_ind(x, y, equal_var=False)
    sp = np.sqrt(((len(x)-1)*x.var(ddof=1) + (len(y)-1)*y.var(ddof=1)) / (len(x)+len(y)-2))
    dd = (x.mean()-y.mean())/sp
    se = np.sqrt(x.var(ddof=1)/len(x) + y.var(ddof=1)/len(y))
    dfw = se**4 / ((x.var(ddof=1)/len(x))**2/(len(x)-1) + (y.var(ddof=1)/len(y))**2/(len(y)-1))
    lo, hi = (x.mean()-y.mean()) + np.array([-1, 1]) * stats.t.ppf(.975, dfw) * se
    u, pu = stats.mannwhitneyu(x, y, alternative="two-sided")
    return {"n_AI": len(x), "n_Base": len(y), "mean_AI": x.mean(), "mean_Base": y.mean(), "diff": x.mean()-y.mean(),
            "ci": [lo, hi], "t": t, "df": dfw, "p": p, "d": dd, "mannwhitney_p": pu}
R["first_period_AER"] = welch(a.aer.values, b.aer.values)
R["first_period_RT"] = welch(a.rt.values, b.rt.values)

# (2) AER adjusted for the reference action of each trial (composition / difficulty control) and order
m = smf.gee("ok ~ ai + C(correct_action) + first", "participant", data=d.reset_index(drop=True), family=sm.families.Binomial()).fit()
R["gee_adjusted_reference_action"] = {"OR_ai": float(np.exp(m.params["ai"])),
    "ci": [float(np.exp(m.conf_int().loc["ai", 0])), float(np.exp(m.conf_int().loc["ai", 1]))], "p": float(m.pvalues["ai"])}

# (3) Difference within each reference-action stratum
st = {}
for k, g in d.groupby("correct_action"):
    x, y = g[g.ai == 1].ok, g[g.ai == 0].ok
    st[k] = {"AER_AI": x.mean(), "AER_Base": y.mean(), "diff": x.mean()-y.mean(), "n_AI": len(x), "n_Base": len(y)}
R["by_reference_action"] = st
# AI AER re-weighted to the baseline reference-action mix (direct standardization)
w = d[d.ai == 0].correct_action.value_counts(normalize=True)
ai_by = d[d.ai == 1].groupby("correct_action").ok.mean()
R["standardized_AI_AER_to_baseline_mix"] = float((ai_by * w).sum())

# (4) Distribution-free checks of the paired difference
R["participants_AI_higher"] = {"higher": int((diff > 0).sum()), "equal": int((diff == 0).sum()), "lower": int((diff < 0).sum()),
    "sign_test_p": float(stats.binomtest(int((diff > 0).sum()), int((diff != 0).sum()), .5).pvalue)}
obs = diff.mean(); signs = rng.choice([-1, 1], size=(20000, len(diff)))
R["paired_permutation_AER_p"] = float(((np.abs((signs * diff.values).mean(axis=1)) >= abs(obs) - 1e-12).mean()))

# (5) Without the 3 most extreme participants on AER difference (leave-extremes-out)
keep = diff.drop(diff.abs().sort_values(ascending=False).index[:3])
R["trimmed_3_most_extreme"] = {"mean_diff": float(keep.mean()), "t": float(stats.ttest_1samp(keep, 0).statistic), "p": float(stats.ttest_1samp(keep, 0).pvalue)}

def clean(o):
    if isinstance(o, dict): return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean(v) for v in o]
    if isinstance(o, (np.floating, np.integer)): return float(o)
    return o
R = clean(R)
(HERE / "robustness.json").write_text(json.dumps(R, indent=1))
fa, fr = R["first_period_AER"], R["first_period_RT"]
md = ["# Robustness analyses (second round)", "",
 f"- First period only (between-subjects, no carry-over): AER {fa['mean_AI']:.3f} (n={fa['n_AI']}) vs {fa['mean_Base']:.3f} (n={fa['n_Base']}), diff {fa['diff']:+.3f} [{fa['ci'][0]:.3f}, {fa['ci'][1]:.3f}], Welch t({fa['df']:.1f}) = {fa['t']:.2f}, p = {fa['p']:.2g}, d = {fa['d']:.2f}; Mann-Whitney p = {fa['mannwhitney_p']:.2g}.",
 f"- First period only, latency: {fr['mean_AI']:.2f} vs {fr['mean_Base']:.2f} s, diff {fr['diff']:+.2f} [{fr['ci'][0]:.2f}, {fr['ci'][1]:.2f}], t = {fr['t']:.2f}, p = {fr['p']:.2g}, d = {fr['d']:.2f}.",
 f"- GEE adjusted for reference action and order: OR = {R['gee_adjusted_reference_action']['OR_ai']:.2f} [{R['gee_adjusted_reference_action']['ci'][0]:.2f}, {R['gee_adjusted_reference_action']['ci'][1]:.2f}], p = {R['gee_adjusted_reference_action']['p']:.2g}.",
 "- AI minus baseline AER within each reference action: " + ", ".join(f"{k} {v['diff']:+.2f}" for k, v in st.items()) + f"; AI AER standardized to the baseline mix: {R['standardized_AI_AER_to_baseline_mix']:.3f}.",
 f"- Participants with higher AER under AI: {R['participants_AI_higher']['higher']}/52 (equal {R['participants_AI_higher']['equal']}, lower {R['participants_AI_higher']['lower']}); sign test p = {R['participants_AI_higher']['sign_test_p']:.2g}; paired permutation p {'< 5e-5' if R['paired_permutation_AER_p']==0 else '= '+format(R['paired_permutation_AER_p'],'.2g')} (20,000 sign flips).",
 f"- Dropping the 3 most extreme participants: mean diff {R['trimmed_3_most_extreme']['mean_diff']:+.3f}, t = {R['trimmed_3_most_extreme']['t']:.2f}, p = {R['trimmed_3_most_extreme']['p']:.2g}."]
(HERE / "robustness.md").write_text("\n".join(md) + "\n")
print("\n".join(md))
