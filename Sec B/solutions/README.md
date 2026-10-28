# Sec B · Worked solutions

All **67 gathered subquestions** have worked answers, including every option in the two “answer any…” questions.

- **[PDF](SOLUTIONS.pdf)** — printable guide with LaTeX equations, matrices, derivations and diagrams.
- **[Markdown](SOLUTIONS.md)** — readable directly on GitHub, which renders the LaTeX math.
- **[HTML preview](SOLUTIONS.html)** — search and navigation with embedded MathML equations; works offline.
- **[LaTeX source](SOLUTIONS.tex)** — generated, editable XeLaTeX document.
- **[Question/page lookup](QUESTION_LOOKUP.csv)** — solution IDs, exam sessions and pages in the solution/original PDFs.

The source answers are in [src/](src/). They use Markdown with `$...$` inline math and `$$...$$` display math; source code examples remain code blocks. The guide groups answers by their primary lecture and also indexes questions spanning multiple sources. Lectures 11–12 now supply the primary references for web injection and UI attacks.

## Rebuild

From the repository root:

```sh
python3 "Sec B/scripts/build.py"
```

Use `--source-only` to regenerate Markdown, HTML and LaTeX without compiling, or `--diagrams` to regenerate the checked-in figure assets as well. See the [repository setup instructions](../../README.md) for Python dependencies and LaTeX packages.

TeX compilation uses XeLaTeX with shell execution disabled. Intermediate files and logs go to `Sec B/_build/`, which Git ignores. PDF navigation/page lookups are rebuilt from LaTeX labels.

## Sources and assumptions

Original question wording/code/figures are in the [past papers](../../CSE405-Security_Merged.pdf). Question summaries in this guide are paraphrases. The answers identify missing query/endpoint assumptions and source issues such as the printed noninvertible Hill key, the cookie flag correction, HMAC block-length normalization and ElGamal message-group distinctions. They are study solutions, not an official marking scheme.
