# Sec B · Computer Security

The section contains **twelve slide decks (Lectures 1–12)**, handwritten notes, a supplementary revision guide, analysis of six final exams and **74 worked entries**.

## Read

1. **[Syllabus and topic list](analysis/SYLLABUS.md)** — complete coverage with slide-page references.
2. **[Final-exam frequency report](analysis/FINAL_EXAM_TOPIC_ANALYSIS.md)** — questions grouped under deck and topic.
3. **[Worked solutions PDF](solutions/SOLUTIONS.pdf)** — equations, matrices, explanations, diagrams and exam tips.
4. [GitHub-readable solution source](solutions/SOLUTIONS.md), [HTML math preview](solutions/SOLUTIONS.html), [LaTeX source](solutions/SOLUTIONS.tex).

[Question lookup](solutions/QUESTION_LOOKUP.csv) links solution IDs to exam questions and PDF pages. The question descriptions are paraphrases; consult the [original papers](../CSE405-Security_Merged.pdf) for exact wording and figures.

## Materials

- [All lecture decks](slides/) — CT4 is no longer a separate folder.
- [Handwritten notes](notes/handwritten-notes.pdf).
- [Supplementary CT4 revision guide](notes/ct4-revision-guide.pdf).

Lectures 11–12 supply the previously missing primary decks for XSS, UI attacks, 2FA, SQL injection, command injection and CAPTCHAs. Lecture 1 now adds security principles, CIA/availability context and six newly solved questions. The updated frequencies include those questions; existing S01–S67 labels are preserved.

## Highest-frequency topic groups

| Topic | Relevant subquestions | Papers |
|---|---:|---:|
| Digital signatures | 8 | 6/6 |
| Classical ciphers | 6 | 5/6 |
| Hashes and collision/birthday attacks | 6 | 4/6 |
| SQL injection | 6 | 4/6 |
| XSS | 6 | 4/6 |
| UI attacks | 5 | 4/6 |
| MAC/HMAC | 5 | 4/6 |
| Security-principle applications (Lecture 1) | 5 | 3/6 |
| Block-cipher modes | 4 | 4/6 |
| Diffie–Hellman/MITM | 4 | 4/6 |

A mixed subquestion can appear under multiple topics. Optional short-note choices and incomplete source coverage are labeled in the detailed analysis.

Build instructions are in the [repository README](../README.md). Editable answer text is in [solutions/src](solutions/src/); generation tools are in [scripts](scripts/).

Both printed sections of every yearly paper are checked by topic; see the [yearly audit](analysis/EXAM_SECTION_AUDIT.csv). The added S74 covers the reflected-XSS case in 2023–24 Q3(a), printed in Section A. Its four network cases belong to the current Sec A guide; the full printed 10 marks are not allocated to the XSS case alone.
