# AlgoPrep

Simple Python practice repo for data structures, algorithms, and interview prep.

Each problem folder usually has:

- a starter implementation file, for example `two_sum.py`
- a matching `test_*.py` file
- a `solution.py` file to compare after you try it

## Setup

Use Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

Run all tests:

```bash
pytest
```

Run one problem:

```bash
pytest ch03_ArraysStringsHashTables/_02_two_sum/
```

## How To Practice

1. Pick a topic folder, such as arrays, linked lists, trees, graphs, or dynamic programming.
2. Open the problem implementation file.
3. Try solving it without looking at `solution.py`.
4. Run that problem's tests.
5. If stuck, read the test cases first, then compare with `solution.py`.
6. Write down the pattern you used so you can recognize it faster next time.

## Good Group Routine

For interview prep with friends:

1. Choose 2 or 3 problems for a session.
2. Timebox each problem to 25-35 minutes.
3. After each attempt, explain the approach out loud.
4. Discuss time and space complexity.
5. Compare solutions and note the pattern.

## Helpful Files

- `PATTERNS.md`: quick guide for recognizing common problem patterns
- `PROGRESS.md`: simple tracker for what has been practiced
- `templates/problem_README.md`: template for documenting new problems

## Topics

- Arrays, strings, and hash tables
- Linked lists
- Stacks and queues
- Trees
- Graphs
- Heaps
- Tries
- Sorting
- Searching
- Dynamic programming
- Bit manipulation
- Extra mixed problems
