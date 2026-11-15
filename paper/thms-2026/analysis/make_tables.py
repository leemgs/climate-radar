"""Writes LaTeX table bodies from results.json next to this script (paste between \\midrule and \\bottomrule of Tables V and VII in main.tex) (tab_primary_rows.tex, tab_subscale_rows.tex)."""
import json
from pathlib import Path
H = Path(__file__).resolve().parent
R = json.loads((H / "results.json").read_text())
M = H.parent / "manuscript"

def p(x):
    return "$<.001$" if x < .001 else f"${x:.3f}$".replace("0.", ".", 1) if x < 1 else "1"

def sgn(x, d):
    s = f"{x:.{d}f}"
    return s.replace("-", "$-$")

def row(r, name, d, dd=None):
    dd = d if dd is None else dd
    return (f"{name} & {r['base_mean']:.{d}f} ({r['base_sd']:.{d}f}) & {r['ai_mean']:.{d}f} ({r['ai_sd']:.{d}f}) & "
            f"{sgn(r['diff'],dd)} [{sgn(r['ci_lo'],dd)}, {sgn(r['ci_hi'],dd)}] & {sgn(r['t'],2)} & {p(r['p_holm'])} & "
            f"{sgn(r['dz'],2)} [{sgn(r['dz_ci_lo'],2)}, {sgn(r['dz_ci_hi'],2)}] \\\\")

S = {r["outcome"]: r for r in R["secondary"]}
L = [r"\multicolumn{7}{l}{\emph{Primary (H1)}} \\", row(R["primary"][0], "AER (proportion)", 2),
     r"\midrule", r"\multicolumn{7}{l}{\emph{Secondary (H2--H4), Holm-adjusted}} \\",
     row(S["Response latency (s)"], "Response latency (s)", 1, 2), row(S["NASA-TLX overall"], "NASA--TLX overall (0--100)", 1),
     row(S["Trust overall"], "Trust overall (1--5)", 2), row(S["SUS"], "SUS, as logged (0--100)", 1)]
(H / "tab_primary_rows.tex").write_text("\n".join(L) + "\n")
names = {"mental_demand": "Mental demand", "physical_demand": "Physical demand", "temporal_demand": "Temporal demand",
         "performance": "Performance", "effort": "Effort", "frustration": "Frustration",
         "trust_reliability": "Perceived reliability", "trust_predictability": "Perceived predictability",
         "trust_appropriateness": "Perceived appropriateness"}
sub = {r["outcome"]: r for r in R["subscales"]}
L = [r"\multicolumn{7}{l}{\emph{NASA--TLX subscales (0--100)}} \\"]
for k in list(names)[:6]: L.append(row(sub[k], names[k], 1))
L += [r"\midrule", r"\multicolumn{7}{l}{\emph{Trust items (1--5)}} \\"]
for k in list(names)[6:]: L.append(row(sub[k], names[k], 2))
(H / "tab_subscale_rows.tex").write_text("\n".join(L) + "\n")
print("ok")
