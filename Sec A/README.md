# Sec A · Computer Security

**11 slide decks (524 PDF pages), an 80-page handwritten notebook, six past exams and 138 worked answers.** Topics span foundations, physical/OS/filesystem security, memory attacks, malware, network/DNS defenses, cryptography and web security.

1. [Syllabus and full source-page map](analysis/SYLLABUS.md).
2. [Ranked exam topics and questions under each deck → exact topic](analysis/FINAL_EXAM_TOPIC_ANALYSIS.md).
3. **[Worked solutions PDF](solutions/SOLUTIONS.pdf)** — typeset equations, diagrams, explanations and exam tips.
4. [Offline HTML with search](solutions/SOLUTIONS.html), [GitHub-readable Markdown](solutions/SOLUTIONS.md), [LaTeX source](solutions/SOLUTIONS.tex).
5. [Question/page lookup](solutions/QUESTION_LOOKUP.csv), [machine-readable question index](analysis/question_index.json).

The analysis checks both printed exam sections because the course split changes by year. Mixed and optional questions retain their original subquestion boundaries; per-topic totals overlap. Partial coverage and supplementary extensions are identified explicitly. The notebook stops at DNS and does not replace the later decks.

Original [slides](slides/) and [notes](notes/) are preserved. The shared [past-paper PDF](../CSE405-Security_Merged.pdf) is the authority for exact question text/code/figures. [Sec B](../Sec%20B/README.md) supplies deeper treatment of several overlapping crypto/web topics.

To rebuild from the repository root, run `python3 "Sec A/scripts/build_reports.py"` then `python3 "Sec A/scripts/build.py"`. Add `--diagrams` to regenerate vector figures. Dependencies and Make targets are documented in the [root README](../README.md).
