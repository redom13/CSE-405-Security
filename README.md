# CSE 405 · Computer Security

Course slides, handwritten notes, analysis of six past final exams and worked solutions, organized by teaching section.

| Section | Syllabus and exam analysis | Worked solutions |
|---|---|---|
| **Sec A** · 9 in-scope decks + 80-page notebook | [Overview](Sec%20A/README.md) · [Syllabus](Sec%20A/analysis/SYLLABUS.md) · [Question frequencies](Sec%20A/analysis/FINAL_EXAM_TOPIC_ANALYSIS.md) | **[PDF](Sec%20A/solutions/SOLUTIONS.pdf)** · [Offline HTML](Sec%20A/solutions/SOLUTIONS.html) · [Markdown](Sec%20A/solutions/SOLUTIONS.md) |
| **Sec B** · Lectures 1–12 + notes/revision guide | [Overview](Sec%20B/README.md) · [Syllabus](Sec%20B/analysis/SYLLABUS.md) · [Question frequencies](Sec%20B/analysis/FINAL_EXAM_TOPIC_ANALYSIS.md) | **[PDF](Sec%20B/solutions/SOLUTIONS.pdf)** · [Offline HTML](Sec%20B/solutions/SOLUTIONS.html) · [Markdown](Sec%20B/solutions/SOLUTIONS.md) |

Sec A has **87 worked entries** (84 whole-question entries and three restricted to Sec A components); Sec B has **74** (including the web-security component of one mixed network/web question). Standalone crypto, number-theory, password-guessing/recovery and web-attack sets are assigned to Sec B and excluded from Sec A. Mixed-question scope and printed-mark limitations are explicit.

**Both printed sections of every yearly paper are checked.** Current section assignment follows topics, because older exam papers interchange the A/B labels. The reports include per-year audits: [Sec A](Sec%20A/analysis/EXAM_SECTION_AUDIT.csv) and [Sec B](Sec%20B/analysis/EXAM_SECTION_AUDIT.csv). General foundations appear in both supplied section materials, so parent-question totals are not additive.

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

`make analysis` refreshes both section reports and inventories. `make source` regenerates Markdown, HTML and LaTeX without compiling PDFs. `make diagrams` regenerates figures and compiles both guides. Use `solutions-a` or `solutions-b` for one section. Each section uses its own answer sources. Sec A does not import Sec B question or solution content.

PDFs use XeLaTeX equations and embedded fonts/vector diagrams. HTML embeds MathML and figures without an external math-rendering service; its source-PDF links work with the repository beside it. Compiler logs, caches, environments and local settings are ignored by Git. Source slides/notes are preserved.
