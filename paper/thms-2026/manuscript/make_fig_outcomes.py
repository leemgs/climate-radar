# Regenerates fig_outcomes_summary.png (Fig. 3) from ../analysis/results.json (written by ../analysis/analyze.py).
# Run from this folder: python3 make_fig_outcomes.py
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = json.loads((Path(__file__).resolve().parent.parent / "analysis" / "results.json").read_text())
rows = {r["outcome"]: r for r in R["primary"] + R["secondary"]}
panels = [("AER (proportion)", "AER", (0, 1.0), "higher is better"),
          ("Response latency (s)", "Response latency (s)", (0, 15), "lower is better"),
          ("NASA-TLX (0-100)", "NASA-TLX overall", (0, 100), "lower is better"),
          ("Trust (1-5)", "Trust overall", (1, 5), "higher is better"),
          ("SUS (0-100)", "SUS", (0, 100), "higher is better")]
plt.rcParams.update({"font.size": 7, "font.family": "serif"})
fig, axes = plt.subplots(1, 5, figsize=(7.0, 1.9))
for ax, (title, key, ylim, note) in zip(axes, panels):
    r = rows[key]
    vals, sds = [r["base_mean"], r["ai_mean"]], [r["base_sd"], r["ai_sd"]]
    xs = [0, 1]
    ax.bar(xs, vals, width=0.6, color=["#bdbdbd", "#525252"], edgecolor="black", linewidth=0.6,
           yerr=sds, capsize=2, error_kw={"linewidth": 0.6})
    ax.set_xticks(xs); ax.set_xticklabels(["Baseline", "AI-assisted"], rotation=20)
    ax.set_ylim(ylim[0], ylim[1] * 1.12 if ylim[0] == 0 else ylim[1] + 0.6); ax.set_title(title, fontsize=7)
    ax.text(0.5, -0.40, note, transform=ax.transAxes, ha="center", fontsize=6, style="italic")
    fmt = "{:.2f}" if key in ("AER", "Trust overall") else "{:.1f}"
    for x, v, sd in zip(xs, vals, sds):
        ax.text(x, v + sd + (ylim[1] - ylim[0]) * 0.02, fmt.format(v), ha="center", va="bottom", fontsize=6)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", labelsize=6, width=0.5, length=2)
fig.tight_layout(w_pad=0.8, pad=0.3)
fig.savefig("fig_outcomes_summary.png", dpi=300)
