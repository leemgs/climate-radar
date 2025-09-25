from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd
from ..config import load_config, ROOT
from ..model.risk_model import fit_composite_risk
from ..llm.recommender import recommend
from ..orchestration.executor import emit_recommendation
from ..orchestration.safety_budgets import within_blast_radius
from ..fairness.audit import eod, ece, aer

def _paths():
    return {
        "data": ROOT/"data"/"synthetic"/"timeseries.csv",
        "results": ROOT/"results",
        "audit_log": ROOT/"audit"/"sample_log.jsonl"
    }

def cmd_fit(cfg):
    p = _paths()
    df = pd.read_csv(p["data"])
    df2, _ = fit_composite_risk(df)
    pth = p["results"]/ "fitted.csv"
    pth.parent.mkdir(parents=True, exist_ok=True)
    df2.to_csv(pth, index=False)
    print(f"[fit] wrote {pth}")

def cmd_recs(cfg):
    p = _paths()
    df = pd.read_csv(p["results"]/ "fitted.csv")
    budget = cfg.thresholds["safety_budgets"]["message_blast_radius"]
    sent = 0
    n = len(df)
    p["audit_log"].write_text("")
    for _, row in df.iterrows():
        frac = sent / max(n,1)
        if not within_blast_radius(frac, budget):
            continue
        rec = recommend(row, dict(policy=cfg.policy, thresholds=cfg.thresholds))
        emit_recommendation(row, rec, cfg.repo_hash, p["audit_log"])
        sent += 1
    print(f"[recs] emitted {sent} recommendations (budget {budget}) to {p['audit_log']}")

def cmd_eval(cfg):
    p = _paths()
    df = pd.read_csv(p["results"]/ "fitted.csv")
    thr = cfg.thresholds["risk_thresholds"]["medium"]
    metrics = {
        "AER": aer(df, thr=thr),
        "ECE": ece(df),
        "EOD_elderly": eod(df, "elderly", thr=thr),
        "EOD_migrant": eod(df, "migrant", thr=thr)
    }
    (p["results"]/ "metrics.json").write_text(json.dumps(metrics, indent=2))
    print("[eval] metrics:", json.dumps(metrics, indent=2))

def cmd_figures(cfg):
    import matplotlib.pyplot as plt
    p = _paths()
    df = pd.read_csv(p["results"]/ "fitted.csv")
    plt.figure()
    df["risk_score"].hist(bins=30)
    plt.title("Risk Score Distribution")
    plt.xlabel("risk_score"); plt.ylabel("count")
    plt.tight_layout()
    plt.savefig(p["results"]/ "fig_risk_hist.png", dpi=160)
    plt.close()

    import numpy as np
    edges = np.linspace(0,1,11)
    mids, accs = [], []
    for i in range(10):
        m = (df["risk_score"]>=edges[i]) & (df["risk_score"]<edges[i+1])
        if m.sum()==0: continue
        mids.append((edges[i]+edges[i+1])/2)
        accs.append(df.loc[m,"action"].mean())
    plt.figure()
    plt.plot([0,1],[0,1], linestyle="--")
    plt.plot(mids, accs, marker="o")
    plt.title("Calibration Plot")
    plt.xlabel("Predicted risk"); plt.ylabel("Observed action rate")
    plt.tight_layout()
    plt.savefig(p["results"]/ "fig_calibration.png", dpi=160)
    plt.close()
    print(f"[figures] wrote plots to {p['results']}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["fit","recs","eval","figures"])
    args = ap.parse_args()
    cfg = load_config()
    if args.step == "fit":
        cmd_fit(cfg)
    elif args.step == "recs":
        cmd_recs(cfg)
    elif args.step == "eval":
        cmd_eval(cfg)
    elif args.step == "figures":
        cmd_figures(cfg)

if __name__ == "__main__":
    main()
