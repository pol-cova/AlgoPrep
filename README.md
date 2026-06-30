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
pytest ch03_ArraysStringsHashTables/_02_two_sum/
```

## Practice

1. Pick a problem from the folder map.
2. Solve the starter file before opening `solution.py`.
3. Run the matching tests.
4. Review the pattern and time/space complexity.

## Folder Map

| Topic | Folder | Problems covered |
| --- | --- | --- |
| Arrays, strings, hash tables | [`ch03_ArraysStringsHashTables`](ch03_ArraysStringsHashTables) | Is Unique, Two Sum, Group Anagrams, Zero Matrix |
| Linked lists | [`ch04_LinkedLists`](ch04_LinkedLists) | Linked list implementation, Remove Duplicates, Merge Two Sorted Lists, Nth Node To Last, Add Two Numbers, Swap Nodes In Pairs |
| Stacks and queues | [`ch05_StacksQueues`](ch05_StacksQueues) | Stack and queue implementation, Queue With Stacks, Valid Parentheses, Sort Stack, Stack Min |
| Trees | [`ch06_Trees`](ch06_Trees) | Binary tree helpers, Invert Binary Tree, List Of Depths, Maximum Depth, Validate BST, Is Subtree, First Common Ancestor |
| Graphs | [`ch07_Graphs`](ch07_Graphs) | Graph search helpers, Route Between Nodes, Clone Graph, Build Order, Number Of Provinces, Redundant Connection |
| Heaps | [`ch08_Heaps`](ch08_Heaps) | Min Heap, Kth Largest Element, Top K Frequent Elements, Relative Ranks |
| Tries | [`ch09_Tries`](ch09_Tries) | Trie implementation, Title Suggestions, Word Search |
| Sorting | [`ch10_Sorting`](ch10_Sorting) | Bubble Sort, Selection Sort, Merge Sort, Quick Sort |
| Searching | [`ch11_Searching`](ch11_Searching) | Binary Search |
| Dynamic programming | [`ch12_DynamicProgramming`](ch12_DynamicProgramming) | Robot In Grid, Set Subsets, Generate Parentheses, Maximum Subarray, Binary Tree Maximum Path Sum |
| Bit manipulation | [`ch13_BitManipulation`](ch13_BitManipulation) | Number Of One Bits, Reverse Integer, Number Conversion, Sum Integers |
| Extra problems | [`ch14_ExtraProblems`](ch14_ExtraProblems) | Merge K Sorted Lists, Word Break, Reverse Nodes In K Group, Longest Unique Substring, House Robber, Coin Change |

## Repo Files

- [`docs.md`](docs.md): pattern cues and practice tracker format
- [`CONTRIBUTING.md`](CONTRIBUTING.md): how to add or update problems
- [`LICENSE`](LICENSE): MIT license
