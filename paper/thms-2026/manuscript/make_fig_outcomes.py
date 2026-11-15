# Regenerates fig_outcomes_summary.png (Fig. 4) from the Table V values. Run from this folder: python3 make_fig_outcomes.py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# Values from Table V of the revised manuscript (means; SD where reported).
panels = [
    ("AER (proportion)", 0.62, 0.81, None, None, (0, 1.0), "higher is better"),
    ("Response latency (s)", 12.4, 8.1, None, None, (0, 15), "lower is better"),
    ("NASA-TLX (0-100)", 59.8, 46.2, 10.9, 9.6, (0, 100), "lower is better"),
    ("Trust (1-5)", 3.4, 4.2, 0.6, 0.5, (1, 5), "higher is better"),
    ("SUS (0-100)", 68.5, 81.7, 11.2, 9.4, (0, 100), "higher is better"),
]
plt.rcParams.update({"font.size": 7, "font.family": "serif"})
fig, axes = plt.subplots(1, 5, figsize=(7.0, 1.9))
for ax, (title, b, a, sb, sa, ylim, note) in zip(axes, panels):
    xs = [0, 1]
    bars = ax.bar(xs, [b, a], width=0.6, color=["#bdbdbd", "#525252"], edgecolor="black", linewidth=0.6,
                  yerr=[sb, sa] if sb is not None else None, capsize=2, error_kw={"linewidth": 0.6})
    ax.set_xticks(xs); ax.set_xticklabels(["Baseline", "AI-assisted"], rotation=20)
    ax.set_ylim(ylim[0], ylim[1] * 1.12 if ylim[0] == 0 else ylim[1] + 0.6); ax.set_title(title, fontsize=7)
    ax.text(0.5, -0.40, note, transform=ax.transAxes, ha="center", fontsize=6, style="italic")
    for x, v, sd in zip(xs, [b, a], [sb, sa]):
        top = v + (sd or 0)
        ax.text(x, top + (ylim[1] - ylim[0]) * 0.02, f"{v:g}", ha="center", va="bottom", fontsize=6)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", labelsize=6, width=0.5, length=2)
fig.tight_layout(w_pad=0.8, pad=0.3)
fig.savefig("fig_outcomes_summary.png", dpi=300)
