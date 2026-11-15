from __future__ import annotations
import argparse, numpy as np, pandas as pd
from pathlib import Path

def generate(n_regions=50, n_timesteps=96, seed=42):
    rng = np.random.default_rng(seed)
    regions = [f"R{i:03d}" for i in range(n_regions)]
    times = np.arange(n_timesteps)
    rows = []
    for r in regions:
        base_hazard = rng.uniform(0.1, 0.7)
        vuln = rng.uniform(0.1, 0.9)
        exposure = rng.uniform(0.2, 0.9)
        social = rng.uniform(0.0, 0.6)
        for t in times:
            h = np.clip(base_hazard + 0.25*np.sin(2*np.pi*(t/96)) + rng.normal(0,0.05), 0, 1)
            e = np.clip(exposure + rng.normal(0,0.05), 0, 1)
            v = np.clip(vuln + rng.normal(0,0.05), 0, 1)
            s = np.clip(social + 0.1*rng.normal(), 0, 1)
            p_act = np.clip(0.2 + 0.4*h + 0.2*e + 0.15*(1-v) + 0.05*s, 0, 1)
            act = rng.binomial(1, p_act)
            rows.append((r, t, h, e, v, s, p_act, act))
    df = pd.DataFrame(rows, columns=["region","t","hazard","exposure","vulnerability","social","p_action_true","action"])
    # subgroup assignment + friction
    sub_rng = np.random.default_rng(seed+1)
    subgroups = sub_rng.choice(["baseline","elderly","migrant"], size=len(df), p=[0.6,0.25,0.15])
    df["subgroup"] = subgroups
    m_e = df["subgroup"]=="elderly"
    m_m = df["subgroup"]=="migrant"
    mask_e1 = m_e & (df["action"]==1)
    n_e = int(mask_e1.sum())
    df.loc[mask_e1, "action"] = (sub_rng.random(n_e)>0.15).astype(int) if n_e>0 else df.loc[mask_e1, "action"]
    mask_m1 = m_m & (df["action"]==1)
    n_m = int(mask_m1.sum())
    df.loc[mask_m1, "action"] = (sub_rng.random(n_m)>0.10).astype(int) if n_m>0 else df.loc[mask_m1, "action"]
    return df

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=str, default="data/synthetic")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    df = generate(seed=args.seed)
    df.to_csv(out/"timeseries.csv", index=False)
    print(f"Wrote {out/'timeseries.csv'} with {len(df)} rows.")

if __name__ == "__main__":
    main()
