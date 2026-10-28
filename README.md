# CSE 405 · Computer Security

Study material, past-final analysis and worked solutions, organized by course section.

- **[Sec B overview](Sec%20B/README.md)**
- **[Sec B worked solutions — PDF](Sec%20B/solutions/SOLUTIONS.pdf)**
- [Sec B syllabus](Sec%20B/analysis/SYLLABUS.md)
- [Past-final question collection](CSE405-Security_Merged.pdf)

## Repository layout

```text
CSE405-Security_Merged.pdf   Shared collection of past final exams
Sec B/
  slides/                   Lectures 02–12, including the former CT4 decks
  notes/                    Handwritten notes and supplementary revision guide
  analysis/                 Syllabus, frequency report, question indices
  solutions/                Worked guide, LaTeX source, Markdown, HTML, figures
  scripts/                  Document build tools
```

Sec A can be added as a separate section using the same layout. All current analysis and solutions concern Sec B.

## Rebuild the guide

On Ubuntu/Debian, install the document tools:

```sh
sudo apt update
sudo apt install texlive-xetex texlive-latex-extra pandoc python3-venv poppler-utils fonts-dejavu-core
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python "Sec B/scripts/build.py"
```

The build generates GitHub-readable Markdown, an HTML math preview, LaTeX source and a PDF. It recompiles LaTeX until the table of contents and navigation references stabilize. The HTML embeds MathML equations for offline reading; the PDF includes its fonts and figures. Build logs, TeX auxiliary files, caches and local environments are ignored by Git.
