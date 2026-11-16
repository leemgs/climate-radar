# Builds the THMS resubmission package into submission/.
#   make            -> manuscript, latexdiff, and letter PDFs
#   make manuscript -> submission/main_revised.pdf
#   make diff       -> submission/main_diff.pdf (and manuscript/main_diff.tex)
#   make letters    -> submission/{cover_letter_en,response_to_reviewers}.pdf
#   make clean      -> remove LaTeX build files
# bibtex exits non-zero because of two known warnings in IEEEtranDOI.bst (name.doi.prefix/postfix); output is unaffected.
# Requires: pdflatex, bibtex, latexdiff, pandoc, Chromium (see letters/make_letter_pdfs.py), fonts-nanum.

MS  := manuscript
SUB := submission
LATEX := pdflatex -interaction=nonstopmode -halt-on-error
DIFFCFG := PICTUREENV=(?:picture|DIFnomarkup|table|table\*|algorithm|figure|figure\*)[\w\d*@]*

.PHONY: all manuscript diff letters clean

all: manuscript diff letters

manuscript:
	cd $(MS) && $(LATEX) main.tex >/dev/null && (bibtex main >/dev/null || true) && $(LATEX) main.tex >/dev/null && $(LATEX) main.tex >/dev/null
	cp $(MS)/main.pdf $(SUB)/main_revised.pdf

diff:
	cd $(MS) && latexdiff -t CFONT --math-markup=0 --config="$(DIFFCFG)" main_original.tex main.tex > main_diff.tex 2>/dev/null
	cd $(MS) && $(LATEX) main_diff.tex >/dev/null && (bibtex main_diff >/dev/null || true) && $(LATEX) main_diff.tex >/dev/null && $(LATEX) main_diff.tex >/dev/null
	cp $(MS)/main_diff.pdf $(SUB)/main_diff.pdf

letters:
	python3 letters/make_letter_pdfs.py

clean:
	cd $(MS) && rm -f *.aux *.log *.bbl *.blg *.out *.toc *.fls *.fdb_latexmk main.pdf main_diff.pdf
