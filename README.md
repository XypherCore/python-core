# python-core

Python phase of **Ascension X**, a 21-phase self-directed technical mastery roadmap. This is Phase 3 (Programming), following [`js-core`](https://github.com/XypherCore/js-core).

## Ground rules

1. Every exercise is written from a blank file, before any reference is opened.
2. A solution that works but that I can't explain at the mechanism level is not done.
3. Reference material is for after a real attempt, never instead of one.
4. One lecture, then its problem set, then a commit, then the next lecture.
5. Capstones must do real work. No tutorial rewrites.

## Scope

Core syntax and idioms, OOP and modular design, file/network/process handling, automation and scripting, and NumPy fundamentals.

**Out of scope:** Pandas, Scikit-learn, and deep learning frameworks. Those belong to the AI/ML phase.

## Repository structure

```
python-core/
├── exercises/
│   ├── day-01-functions-variables/
│   │   ├── indoor_voice.py
│   │   └── notes.md
│   ├── day-02-conditionals/
│   └── ...
├── projects/
│   └── <capstone-name>/
├── .gitignore
└── README.md
```

- `exercises/day-XX-topic/`: one folder per day. Blind attempts, plus a `notes.md` when a concept needed a second pass or a mechanism question exposed a gap.
- `projects/`: one folder per capstone, each with its own README.

## Curriculum

Lecture numbers refer to the CS50P course. Day counts are starting points and move if a block exposes a real gap.

### Block 1: Foundations

| Day | Topic | CS50P | Folder |
|---|---|---|---|
| 01 | Functions, variables | L0 | `day-01-functions-variables` |
| 02 | Conditionals | L1 | `day-02-conditionals` |
| 03 | Loops | L2 | `day-03-loops` |
| 04 | Exceptions | L3 | `day-04-exceptions` |
| 05 | Libraries and packages | L4 | `day-05-libraries` |
| 06 | Unit tests | L5 | `day-06-unit-tests` |
| 07 | File I/O | L6 | `day-07-file-io` |
| 08 | Regular expressions | L7 | `day-08-regex` |

### Block 2: OOP and modular design

| Day | Topic | Source | Folder |
|---|---|---|---|
| 09 | Classes, instances, properties | L8 | `day-09-oop-basics` |
| 10 | Comprehensions, `*args`/`**kwargs`, unpacking, generators, type hints | L9 | `day-10-idioms` |
| 11 | Dunder methods | Python docs, ABTS | `day-11-dunder-methods` |
| 12 | Inheritance and MRO | Python docs | `day-12-inheritance-mro` |
| 13 | Decorators, context managers, packaging | Python docs | `day-13-decorators-context-managers` |

### Block 3: File, network, process

| Day | Topic | Folder |
|---|---|---|
| 14 | `pathlib`, `os`, `sys` | `day-14-pathlib-os-sys` |
| 15 | Sockets | `day-15-sockets` |
| 16 | `subprocess` | `day-16-subprocess` |

### Block 4: Automation and scripting

| Day | Topic | Folder |
|---|---|---|
| 17 | CLI tools with `argparse` | `day-17-cli-argparse` |
| 18 | Filesystem automation and scheduling | `day-18-fs-automation` |

### Block 5: Numerical computing

| Day | Topic | Folder |
|---|---|---|
| 19 | NumPy arrays and indexing | `day-19-numpy-arrays` |
| 20 | Vectorized thinking, broadcasting | `day-20-vectorization` |

### Block 6: Capstones

Day 21 onward. 2-3 projects, defined at the start of the block, not before.

## Resources

| Resource | Role |
|---|---|
| CS50P (Harvard) | Primary source and problem sets |
| Automate the Boring Stuff | Practical reference for the OOP and automation blocks |
| Python docs (`docs.python.org`) | Reference for dunders, MRO, decorators, stdlib modules |

## Progress

A box is ticked only when the day's work is committed.

**Block 1: Foundations**
- [x] Day 01: Functions, variables
- [ ] Day 02: Conditionals
- [ ] Day 03: Loops
- [ ] Day 04: Exceptions
- [ ] Day 05: Libraries and packages
- [ ] Day 06: Unit tests
- [ ] Day 07: File I/O
- [ ] Day 08: Regular expressions

**Block 2: OOP and modular design**
- [ ] Day 09: OOP basics
- [ ] Day 10: Idioms
- [ ] Day 11: Dunder methods
- [ ] Day 12: Inheritance and MRO
- [ ] Day 13: Decorators, context managers, packaging

**Block 3: File, network, process**
- [ ] Day 14: `pathlib`, `os`, `sys`
- [ ] Day 15: Sockets
- [ ] Day 16: `subprocess`

**Block 4: Automation and scripting**
- [ ] Day 17: CLI tools
- [ ] Day 18: Filesystem automation

**Block 5: Numerical computing**
- [ ] Day 19: NumPy arrays
- [ ] Day 20: Vectorization

**Block 6: Capstones**
- [ ] Capstone 1
- [ ] Capstone 2

## Setup

Requires Python 3.11+.

```bash
python3 --version
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
pip install cowsay requests     # first needed on Day 05
pip freeze > requirements.txt
deactivate
```

Days 01-04 are stdlib-only and need no venv. Day 05 is the first that does. `venv/` is never committed.

## Workflow

- One commit per completed day, after the day's work is done, not mid-session.
- Commit format: `Day XX: <topic>`
- Capstone commits: `<project>: <what changed>`

## Related

- [`js-core`](https://github.com/XypherCore/js-core): the JavaScript phase

Built under [XypherCore](https://github.com/XypherCore).
