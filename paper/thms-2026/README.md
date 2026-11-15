# IEEE THMS Resubmission (THMS-26-02-0115, Reject & Resubmit)

**Title:** *From Alerts to Actions: An Action-Centered Human–AI Decision Support Framework for Disaster Response*
**Previous title:** *From Alerts to Actions: A Human–AI Decision System for Reliable Action Execution Under Disaster Risk*
**Decision letter:** 12 November 2026 (Dr. L. Trajkovic, Editor-in-Chief). A new submission must include a letter that answers the decision letter.

## 📤 Files to upload (`submission/`)

| File | Upload as |
|---|---|
| [`submission/main_revised.pdf`](./submission/main_revised.pdf) | Manuscript (13 pages) |
| [`submission/cover_letter_en.pdf`](./submission/cover_letter_en.pdf) | Cover letter (references the decision letter) |
| [`submission/response_to_reviewers.pdf`](./submission/response_to_reviewers.pdf) | Point-by-point response to the AE and reviewers |
| [`submission/main_diff.pdf`](./submission/main_diff.pdf) | Marked-up comparison with the previous submission (supplementary) |

LaTeX source for upload (if requested): the contents of `manuscript/`. `main.tex` is the main file; it needs the `.bib`, `.bst`, `.cls`, the `095_reference.tex` input, and the figures `fig_outcomes_summary.png`. Figs. 1–2 are drawn in TikZ inside `main.tex`.

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
│   ├── fig_outcomes_summary.png  (+ make_fig_outcomes.py to regenerate it)
│   └── fig_*.png         # figures used only by main_original.tex
├── letters/              # Markdown sources of cover letters and responses (EN/KO)
│   └── make_letter_pdfs.py  # Markdown -> PDF (EN to submission/, KO copies here)
└── notes/
    └── reviewer_risk_assessment_ko.md  # reviewer-perspective risk assessment
```

## 🔧 Rebuild

```bash
cd paper/thms-2026
make            # manuscript + latexdiff + letter PDFs into submission/
make clean      # remove LaTeX build files
```

Requires `pdflatex`, `bibtex`, `latexdiff`, `pandoc`, a Chromium/Chrome binary (path via `CHROME`), and a Korean font (`fonts-nanum`) for the Korean copies.

## ⚠️ Known limitations of this submission
The user study was conducted several months before this revision, and its trial-level raw data are no longer available. Exact test statistics, confidence intervals, d_z, and the AER decomposition could therefore not be reported. These are stated in §VII-D of the manuscript and in the response letter. See [`notes/reviewer_risk_assessment_ko.md`](./notes/reviewer_risk_assessment_ko.md) for the expected reviewer concerns.
