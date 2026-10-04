# python-core

Python phase of **Ascension X**, a 21-phase self-directed technical mastery roadmap. This is Phase 3 (Programming), following [`js-core`](https://github.com/XypherCore/js-core).

## Ground rules

1. Every exercise is written from a blank file, before any reference is opened.
2. A solution that works but that I can't explain at the mechanism level is not done.
3. Reference material is for after a real attempt, never instead of one.
4. Capstones must do real work. No tutorial rewrites.

## Scope

Core syntax and idioms, OOP and modular design, file/network/process handling, automation and scripting, and NumPy fundamentals.

**Out of scope:** Pandas, Scikit-learn, and deep learning frameworks. Those belong to the AI/ML phase and are deliberately not pulled in here.

## Repository structure

```
python-core/
├── exercises/
│   ├── day-01-functions-idioms/
│   │   ├── grade.py
│   │   ├── evens.py
│   │   └── notes.md
│   ├── day-02-control-flow-sequences/
│   └── ...
├── projects/
│   └── <capstone-name>/
├── .gitignore
└── README.md
```

- `exercises/day-XX-topic/`: one folder per day. Blind attempts, plus a `notes.md` when a concept needed a second pass or a mechanism question exposed a gap.
- `projects/`: one folder per capstone, each with its own README.

## Curriculum

Day counts are starting points and move if a block exposes a real gap.

### Block 1: Foundations (Days 01-07)

| Day | Topic |
|---|---|
| 01 | Functions, variables, Python idioms (chained comparisons, `*args`, unpacking) |
| 02 | Conditionals, loops, sequences, comprehensions |
| 03 | Exceptions and error handling |
| 04 | Libraries, modules, imports |
| 05 | Unit testing |
| 06 | File I/O |
| 07 | Regular expressions |

### Block 2: OOP and modular design (Days 08-11)

| Day | Topic |
|---|---|
| 08 | Classes, instances, properties, class vs instance state |
| 09 | The data model: dunder methods |
| 10 | Inheritance and MRO |
| 11 | Decorators, context managers, packaging |

### Block 3: File, network, process (Days 12-14)

| Day | Topic |
|---|---|
| 12 | `pathlib`, `os`, `sys` |
| 13 | Sockets |
| 14 | `subprocess` |

### Block 4: Automation and scripting (Days 15-16)

| Day | Topic |
|---|---|
| 15 | CLI tools with `argparse` |
| 16 | Filesystem automation and scheduling |

### Block 5: Numerical computing (Days 17-18)

| Day | Topic |
|---|---|
| 17 | NumPy arrays and indexing |
| 18 | Vectorized thinking, broadcasting |

### Block 6: Capstones (Day 19+)

2-3 projects, defined at the start of the block, not before.

## Resources

| Resource | Role |
|---|---|
| CS50P (Harvard) | Primary source and problem sets |
| Automate the Boring Stuff | Practical reference for the OOP and automation blocks |

## Progress

- [ ] Block 1: Foundations
- [ ] Block 2: OOP and modular design
- [ ] Block 3: File, network, process
- [ ] Block 4: Automation and scripting
- [ ] Block 5: Numerical computing
- [ ] Block 6: Capstones

## Setup

Requires Python 3.11+.

```bash
python3 --version
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
pip install -r requirements.txt # once the file exists
deactivate
```

Stdlib-only days need no venv. `venv/` is never committed.

## Workflow

- One commit per completed day, after the day's work is done, not mid-session.
- Commit format: `Day XX: <topic>`
- Capstone commits: `<project>: <what changed>`

## Related

- [`js-core`](https://github.com/XypherCore/js-core): the JavaScript phase

Built under [XypherCore](https://github.com/XypherCore).