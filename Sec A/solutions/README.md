# Sec A worked solutions

**87 worked entries: 84 whole-question entries and three restricted to Sec A components.** Questions are selected by current topic across both printed sections of all six yearly papers. Standalone Sec B crypto/web question sets are excluded.

- **[Typeset PDF](SOLUTIONS.pdf)** for reading and printing.
- [Offline HTML](SOLUTIONS.html) with search, native MathML and embedded figures.
- [Markdown](SOLUTIONS.md), [generated LaTeX](SOLUTIONS.tex) and [question/page lookup](QUESTION_LOOKUP.csv).

Mixed-question scope and printed-mark limitations are explicit. Existing identifiers stay stable, so removed answers leave gaps. These are independent worked study answers; consult the original paper for exact code and figures.

Answer text and metadata are in [src/new_questions.py](src/new_questions.py). [questions.py](../scripts/questions.py) validates the Sec A scope and attaches preserved IDs from [solution_ids.json](../scripts/solution_ids.json). [catalog.py](../scripts/catalog.py) defines active topics and excludes older crypto/web source material. No Sec B answer generator is loaded.

Build with `python3 "Sec A/scripts/build.py"`; use `--source-only` to skip XeLaTeX or `--diagrams` to regenerate figures. Refresh reports with `python3 "Sec A/scripts/build_reports.py"`. Source-page coverage and the printed-section audit are in the [analysis](../analysis/FINAL_EXAM_TOPIC_ANALYSIS.md).
