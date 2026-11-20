# IEEE THMS Resubmission (THMS-26-02-0115, Reject & Resubmit)

**Title:** *From Alerts to Actions: An Action-Centered Human–AI Decision Support Framework for Disaster Response*
**Previous title:** *From Alerts to Actions: A Human–AI Decision System for Reliable Action Execution Under Disaster Risk*
**Decision letter:** 12 November 2026 (Dr. L. Trajkovic, Editor-in-Chief). A new submission must include a letter that answers the decision letter.

## 📤 Files to upload (`submission/`)

| File | Upload as |
|---|---|
| [`submission/main_revised.pdf`](./submission/main_revised.pdf) | Manuscript (10 pages, incl. references; THMS regular-paper limit) |
| [`submission/cover_letter_en.pdf`](./submission/cover_letter_en.pdf) | Cover letter (references the decision letter) |
| [`submission/response_to_reviewers.pdf`](./submission/response_to_reviewers.pdf) | Point-by-point response to the AE and reviewers |
| [`submission/main_diff.pdf`](./submission/main_diff.pdf) | Marked-up comparison with the previous submission (supplementary) |
| [`submission/supplementary_material.pdf`](./submission/supplementary_material.pdf) | Optional supplementary material (interface spec, scenarios, training, questionnaires, prototype configuration from the author's documentation; S8 adds materials re-created from backup, labelled as post hoc reconstruction) |

LaTeX source for upload (if requested): the contents of `manuscript/`. `main.tex` is the main file; it needs the `.bib`, `.bst`, `.cls`, the `095_reference.tex` input, `main.tex` has no external figures: Figs. 1–2 are drawn in TikZ inside it.

## 📁 Layout

```
thms-2026/
├── README.md
├── Makefile              # make: rebuild everything into submission/
├── submission/           # final PDFs to upload (generated)
├── manuscript/           # LaTeX source
│   ├── main.tex          # revised manuscript
│   ├── main_original.tex # previous submission (for latexdiff)
│   ├── main_diff.tex     # latexdiff output (generated)
│   ├── reference-data.bib, IEEEtran.cls, IEEEtranDOI.bst, 095_reference.tex
│   ├── fig_outcomes_summary.png  (+ make_fig_outcomes.py; no longer used by main.tex)
│   └── fig_*.png         # figures used only by main_original.tex
├── letters/              # Markdown sources of the cover letter and the response to reviewers (English only)
│   └── make_letter_pdfs.py  # Markdown -> PDF (English PDFs to submission/)
└── notes/
    └── reviewer_risk_assessment.md  # reviewer-perspective risk assessment
```

## 🔧 Rebuild

```bash
cd paper/thms-2026
make            # manuscript + latexdiff + letter PDFs into submission/
make clean      # remove LaTeX build files
```

Requires `pdflatex`, `bibtex`, `latexdiff`, `pandoc`, a Chromium/Chrome binary (path via `CHROME`).

## ⚠️ Known limitations of this submission
The anonymized trial-level logs and questionnaire records (`data/`) were re-analyzed with `analysis/analyze.py`, and every reported statistic comes from that script. The author's prototype documentation (`docs/` at the repository root) was added on 2026-11-17 and now supplies the interface layout, scenario type, training flow, trust-item wording and the risk-model/guardrail configuration. What is still not documented (per-trial stimulus values, how the reference action was derived, per-trial time limit, total training length and pass criterion, τ_u/τ_c and the criticality scale, how escalation was triggered, interface screenshots) is listed in §VII-D of the manuscript and in the response letter. The records also show properties that readers will notice (a constant, condition-specific offset in the logged SUS totals; very small between-participant latency variance; scenario labels that do not map to reference actions); these are disclosed in §IV-F and §VII-D and analyzed in [`notes/data_audit.md`](./notes/data_audit.md). The author confirmed on 2026-11-16 that the records are the original study data. See [`notes/reviewer_risk_assessment.md`](./notes/reviewer_risk_assessment.md) for the expected reviewer concerns.

## 🗂️ Materials recovered from backup (added 2026-11-20)
The author recovered and re-created experiment materials from backup storage. They are in [`data/reconstructed/`](./data/reconstructed/README.md) and appear only in Supplementary S8 as **post hoc reconstruction**. They do not match the primary trial log at trial level (same selected action in 22% of matched trials; 208 vs. 150 escalated trials), so no manuscript result uses them; see [`notes/reconstructed_reconciliation.md`](./notes/reconstructed_reconciliation.md). **Pending (needs LaTeX, not installed in the cloud session):** add the sentence in that note to §VII-D of `manuscript/main.tex` and rebuild `submission/main_revised.pdf`.
