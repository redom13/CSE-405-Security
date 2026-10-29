# Sec A · Computer Security

**87 worked entries across six past exams**, covering foundations, physical/OS/filesystem security, memory attacks, malware and network/DNS/IDS defenses. There are **9 in-scope decks (415 PDF pages)** and an 80-page handwritten notebook. Two older crypto/web PDFs remain preserved as references outside this study scope.

1. [Sec A syllabus and source-page map](analysis/SYLLABUS.md).
2. [Ranked questions under deck → exact topic](analysis/FINAL_EXAM_TOPIC_ANALYSIS.md).
3. **[Worked solutions PDF](solutions/SOLUTIONS.pdf)** — typeset equations, diagrams, reasoning and exam tips.
4. [Offline HTML with search](solutions/SOLUTIONS.html), [Markdown](solutions/SOLUTIONS.md), [LaTeX source](solutions/SOLUTIONS.tex).
5. [Question/page lookup](solutions/QUESTION_LOOKUP.csv), [question index](analysis/question_index.json), [yearly printed-section audit](analysis/EXAM_SECTION_AUDIT.csv).

**Questions are assigned by current topic, not the printed Section A/B label. Both sections of every yearly paper are checked.** For example, the physical-lock questions printed in Section B of 2018–19 belong here. The crypto questions printed in Section A of 2021–22 belong in the current Sec B guide.

This guide has 84 whole-question entries and three entries restricted to their Sec A components. Scope notes identify omitted Sec B tasks and distinguish the original printed marks from the retained components. Existing solution IDs are preserved, leaving numbering gaps where unrelated entries were removed.

Standalone cryptographic algorithms, number theory, password-guessing/recovery and web-attack sets are excluded from Sec A. The [syllabus](analysis/SYLLABUS.md) records the boundary for mixed source files. Original [slides](slides/) and [notes](notes/) are preserved; the [past papers](../CSE405-Security_Merged.pdf) supply exact question text/code/figures.

Rebuild from the repository root:

```sh
python3 "Sec A/scripts/build_reports.py"
python3 "Sec A/scripts/build.py"
```

The section uses its own answer sources, stylesheet and figures. It does not import Sec B answers. Use `--diagrams` to regenerate its figures. Setup is documented in the [root README](../README.md).
