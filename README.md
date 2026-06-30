# AlgoPrep

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Tests](https://img.shields.io/badge/tests-pytest-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Python practice repo for data structures, algorithms, and interview prep.

Each problem folder has a starter file, tests, and usually a `solution.py` to compare after you try it.

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
pytest arrays_hashing/two_sum/
```

## Practice

1. Pick a problem from the folder map.
2. Solve the starter file before opening `solution.py`.
3. Run the matching tests.
4. Review the pattern and time/space complexity.

## Folder Map

| Topic | Folder | Problems covered |
| --- | --- | --- |
| Arrays, strings, hash tables | [`arrays_hashing`](arrays_hashing) | Is Unique, Two Sum, Group Anagrams, Zero Matrix |
| Linked lists | [`linked_lists`](linked_lists) | Linked list implementation, Remove Duplicates, Merge Two Sorted Lists, Nth Node To Last, Add Two Numbers, Swap Nodes In Pairs |
| Stacks and queues | [`stacks_queues`](stacks_queues) | Stack and queue implementation, Queue With Stacks, Valid Parentheses, Sort Stack, Stack Min |
| Trees | [`trees`](trees) | Binary tree helpers, Invert Binary Tree, List Of Depths, Maximum Depth, Validate BST, Is Subtree, First Common Ancestor |
| Graphs | [`graphs`](graphs) | Graph search helpers, Route Between Nodes, Clone Graph, Build Order, Number Of Provinces, Redundant Connection |
| Heaps | [`heaps`](heaps) | Min Heap, Kth Largest Element, Top K Frequent Elements, Relative Ranks |
| Tries | [`tries`](tries) | Trie implementation, Title Suggestions, Word Search |
| Sorting | [`sorting`](sorting) | Bubble Sort, Selection Sort, Merge Sort, Quick Sort |
| Searching | [`searching`](searching) | Binary Search |
| Dynamic programming | [`dynamic_programming`](dynamic_programming) | Robot In Grid, Set Subsets, Generate Parentheses, Maximum Subarray, Binary Tree Maximum Path Sum |
| Bit manipulation | [`bit_manipulation`](bit_manipulation) | Number Of One Bits, Reverse Integer, Number Conversion, Sum Integers |
| Extra problems | [`extra_problems`](extra_problems) | Merge K Sorted Lists, Word Break, Reverse Nodes In K Group, Longest Unique Substring, House Robber, Coin Change |

## Repo Files

- [`docs.md`](docs.md): pattern cues and practice tracker format
- [`CONTRIBUTING.md`](CONTRIBUTING.md): how to add or update problems
- [`LICENSE`](LICENSE): MIT license
