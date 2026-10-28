# CSE 405 · Computer Security

Course slides, handwritten notes, analysis of six past final exams and worked solutions, organized by teaching section.

| Section | Syllabus and exam analysis | Worked solutions |
|---|---|---|
| **Sec A** · 11 decks + 80-page notebook | [Overview](Sec%20A/README.md) · [Syllabus](Sec%20A/analysis/SYLLABUS.md) · [Question frequencies](Sec%20A/analysis/FINAL_EXAM_TOPIC_ANALYSIS.md) | **[PDF](Sec%20A/solutions/SOLUTIONS.pdf)** · [Offline HTML](Sec%20A/solutions/SOLUTIONS.html) · [Markdown](Sec%20A/solutions/SOLUTIONS.md) |
| **Sec B** · Lectures 1–12 + notes/revision guide | [Overview](Sec%20B/README.md) · [Syllabus](Sec%20B/analysis/SYLLABUS.md) · [Question frequencies](Sec%20B/analysis/FINAL_EXAM_TOPIC_ANALYSIS.md) | **[PDF](Sec%20B/solutions/SOLUTIONS.pdf)** · [Offline HTML](Sec%20B/solutions/SOLUTIONS.html) · [Markdown](Sec%20B/solutions/SOLUTIONS.md) |

Sec A has **138** mapped questions and Sec B has **73**. Some crypto/web/principle questions appear in both guides because the teaching materials overlap. There are 60 shared question labels, giving [151 distinct mapped questions](Sec%20A/analysis/CROSS_SECTION_COVERAGE.csv) across the two guides. These counts are not additive. Every mapped question has a complete worked answer, explanations, assumptions and exam tips. Counts include related extensions and optional choices, labeled in the detailed reports.

[Original past-final collection](CSE405-Security_Merged.pdf) remains at the root as a shared source. Questions are mapped by subject matter across both printed exam sections; older papers use different teaching splits. Summaries are paraphrases; source pages supply exact wording, code and diagrams.

```text
CSE405-Security_Merged.pdf
Sec A/ or Sec B/
  slides/       Original lecture PDFs
  notes/        Original handwritten/supplementary PDFs
  analysis/     Syllabus, frequency report, question CSV/JSON, inventory
  solutions/    Compiled PDF, LaTeX, Markdown, offline HTML, figures, lookup
  scripts/      Reproducible document builders
  _build/       Ignored extraction caches, previews and compiler logs
```

## Rebuild

On Ubuntu/Debian:

```sh
sudo apt install texlive-xetex texlive-latex-extra pandoc python3-venv poppler-utils fonts-dejavu-core
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make PYTHON=.venv/bin/python solutions
```

`make analysis` refreshes both section reports and inventories. `make source` regenerates Markdown, HTML and LaTeX without compiling PDFs. `make diagrams` regenerates figures and compiles both guides. Use `solutions-a` or `solutions-b` for one section. Sec A reuses the matching checked Sec B answer sources for shared questions; keep the repository together when rebuilding.

PDFs use XeLaTeX equations and embedded fonts/vector diagrams. HTML embeds MathML and figures without an external math-rendering service; its source-PDF links work with the repository beside it. Compiler logs, caches, environments and local settings are ignored by Git. Source slides/notes are preserved.
