# Converts the cover letters and responses to reviewers (Markdown) into PDFs for submission.
# Internal repository notes (file lists, resubmission checklists, cross-file pointers) are removed.
# Requires: pandoc, a Chromium/Chrome binary (set CHROME, default /opt/pw-browsers/chromium/chrome-linux64/chrome),
# and a Korean font (e.g., fonts-nanum).
# Run from this folder: python3 make_letter_pdfs.py
import os
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome")

CSS = """
@page { size: A4; margin: 22mm 20mm 22mm 20mm; }
body { font-family: 'Times New Roman', 'Nanum Myeongjo', 'NanumMyeongjo', serif; font-size: 11pt; line-height: 1.45; color: #000; }
body.cover { font-size: 10pt; line-height: 1.3; }
body.cover p { margin: 0 0 7pt; } body.cover li { margin-bottom: 3pt; } body.cover hr { margin: 8pt 0; }
body.cover.ko { font-size: 10pt; line-height: 1.5; }
body.ko { font-family: 'NanumGothic', 'Nanum Gothic', sans-serif; font-size: 10.5pt; line-height: 1.6; }
h1 { font-size: 16pt; margin: 0 0 10pt; }
h2 { font-size: 13pt; margin: 18pt 0 6pt; border-bottom: 1px solid #999; padding-bottom: 2pt; }
h3 { font-size: 11.5pt; margin: 14pt 0 4pt; }
p, li { text-align: justify; }
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 6pt 0 10pt; }
th, td { border: 1px solid #888; padding: 4pt 5pt; vertical-align: top; text-align: left; }
th { background: #eee; }
blockquote { margin: 6pt 0; padding: 4pt 10pt; border-left: 3px solid #999; color: #333; }
hr { border: none; border-top: 1px solid #bbb; margin: 12pt 0; }
code { font-size: 9.5pt; }
"""


def strip_sections(md, headings):
    """Remove each '## heading' / '### heading' section up to the next heading of the same or higher level."""
    for h in headings:
        m = re.search(r"^(#+) " + re.escape(h) + r"\s*$", md, flags=re.M)
        if not m:
            raise SystemExit(f"heading not found: {h}")
        nxt = re.compile(r"^#+ ", flags=re.M)  # stop at the next heading of any level
        n = nxt.search(md, m.end())
        md = md[: m.start()] + (md[n.start():] if n else "")
    return md


def clean_cover(md):
    md = re.sub(r"\A# .*\n+", "", md)          # file title
    md = re.sub(r"\A> .*\n+", "", md)          # internal note
    md = re.sub(r"\A---\n+", "", md)           # leading rule
    return md


def clean_response(md, lang):
    if lang == "en":
        md = strip_sections(md, ["Files in this folder", "Cover letter"])
        md = re.sub(r"^> \*\*Before resubmission:\*\*.*\n+", "", md, flags=re.M)
        md = re.sub(r" If a check later shows[^\n]*", "", md)
    else:
        md = strip_sections(md, ["이 폴더의 파일", "커버레터"])
        md = re.sub(r"^> \*\*재제출 준비:\*\*.*\n+", "", md, flags=re.M)
        md = re.sub(r" 나중에 본문 값이[^\n]*", "", md)
    md = re.sub(r"\n---\n(\s*\n---\n)+", "\n---\n", md)  # collapse rules left by removed sections
    return md


JOBS = [
    ("cover_letter_en.md", "cover_letter_en.pdf", "en cover", clean_cover, "Cover Letter"),
    ("cover_letter_ko.md", "cover_letter_ko.pdf", "ko cover", clean_cover, "커버레터"),
    ("response_to_reviewers.md", "response_to_reviewers.pdf", "en", lambda m: clean_response(m, "en"), "Response to Reviewers"),
    ("response_to_reviewers_ko.md", "response_to_reviewers_ko.pdf", "ko", lambda m: clean_response(m, "ko"), "리뷰어 응답서"),
]


def main():
    with tempfile.TemporaryDirectory() as tmp:
        for src, out, lang, clean, title in JOBS:
            md = clean((HERE / src).read_text(encoding="utf-8"))
            mdfile = Path(tmp) / src
            mdfile.write_text(md, encoding="utf-8")
            html = subprocess.run(
                ["pandoc", str(mdfile), "-f", "gfm+hard_line_breaks" if "cover" in lang else "gfm",
                 "-t", "html5", "--standalone",
                 "--metadata", f"pagetitle={title}"],
                check=True, capture_output=True, text=True).stdout
            html = html.replace("<body>", f'<body class="{lang}">').replace("</head>", f"<style>{CSS}</style></head>")
            htmlfile = Path(tmp) / (src + ".html")
            htmlfile.write_text(html, encoding="utf-8")
            subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                            "--no-pdf-header-footer", f"--print-to-pdf={HERE / out}",
                            htmlfile.as_uri()], check=True, capture_output=True)
            print("wrote", out)


if __name__ == "__main__":
    main()
