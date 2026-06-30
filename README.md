# kata

Python practice problems for data structures and algorithms.

Exercises are grouped by topic in chapter folders. Each exercise includes a starter file and pytest tests.

Use this repo to practice two skills:

- implementing common DSA problems
- recognizing the pattern a problem is testing

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

Run everything:

```bash
pytest
```

Run one exercise:

```bash
pytest ch03_ArraysStringsHashTables/_01_is_unique/
```

## Practice flow

1. Open an exercise file.
2. Replace `raise NotImplementedError` with your solution.
3. Run the matching test file.

## Study resources

- [PATTERNS.md](PATTERNS.md): quick pattern recognition guide
- [PROGRESS.md](PROGRESS.md): simple practice tracker
- [templates/problem_README.md](templates/problem_README.md): template for documenting each exercise
