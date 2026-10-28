# Sec A worked solutions

All **138 indexed questions** have full answers, including every task of mixed questions and all choices in included optional short-note questions. There are **84 newly developed system/network/general-security answers** and **54 shared questions** whose checked answer text is also present in Sec B. Six of the new principle answers are also included in the updated Sec B guide, so 60 question labels are shared overall.

- **[Typeset PDF](SOLUTIONS.pdf)** for reading and printing.
- [Offline HTML](SOLUTIONS.html) with search, native MathML and embedded diagrams.
- [Markdown](SOLUTIONS.md) for GitHub reading/editing and [generated LaTeX](SOLUTIONS.tex).
- [Lookup CSV](QUESTION_LOOKUP.csv) with exam pages and compiled answer-page numbers.

The guide explains under-specified premises, calling-convention assumptions, probability models and limits of security mechanisms. These are independent study answers, not an official marking scheme. Read the linked original paper for exact code and figures.

New answer text and metadata are in [src/new_questions.py](src/new_questions.py). [questions.py](../scripts/questions.py) selects matching Sec B answers and maps all questions to Sec A topics. [catalog.py](../scripts/catalog.py) records the deck/notes page map. Build from the repository root with `python3 "Sec A/scripts/build.py"`; use `--source-only` to skip XeLaTeX, or `--diagrams` to regenerate figures. Refresh analysis separately with `python3 "Sec A/scripts/build_reports.py"`.
