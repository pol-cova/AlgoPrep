# Contributing

Contributions should keep the repo easy to use for interview practice.

## Add A Problem

1. Put the problem in the matching topic folder.
2. Use a short snake_case folder name, for example `_05_valid_palindrome`.
3. Add a starter implementation file.
4. Add a `test_*.py` file with clear examples and edge cases.
5. Add `solution.py` only after the starter and tests are ready.
6. Update the folder map in `README.md`.

## Problem Folder Shape

```text
_NN_problem_name/
  __init__.py
  problem_name.py
  solution.py
  test_problem_name.py
```

## Before Opening A Pull Request

Run:

```bash
pytest
```

Keep changes focused. Avoid unrelated formatting, generated files, and local environment files.
