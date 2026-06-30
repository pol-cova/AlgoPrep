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

## Usage

Run every test from the repo root:

```bash
pytest
```

Work on one problem:

```bash
cd arrays_hashing/two_sum
pytest
```

## Practice

1. Pick a topic folder, then enter a problem folder.
2. Solve the starter file before opening `solution.py`.
3. Run `pytest` from that problem folder.
4. Write down the pattern and time/space complexity.

## Folder Map

| Topic | Folder | Common patterns | Problems |
| --- | --- | --- | --- |
| Arrays, strings, hash tables | [`arrays_hashing`](arrays_hashing) | hash map, sets, frequency counts | Is Unique, Two Sum, Group Anagrams, Zero Matrix |
| Sliding window | [`sliding_window`](sliding_window) | fixed window, variable window, frequency counts | Longest Repeating Character Replacement |
| Prefix sum | [`prefix_sum`](prefix_sum) | running sum, subarray counts | Subarray Sum Equals K |
| Intervals | [`intervals`](intervals) | sorting, merging ranges | Merge Intervals |
| Linked lists | [`linked_lists`](linked_lists) | pointers, dummy nodes, runner technique | Linked list implementation, Remove Duplicates, Merge Two Sorted Lists, Nth Node To Last, Add Two Numbers, Swap Nodes In Pairs |
| Stacks and queues | [`stacks_queues`](stacks_queues) | stack, queue, monotonic thinking | Stack and queue implementation, Queue With Stacks, Valid Parentheses, Sort Stack, Stack Min |
| Trees | [`trees`](trees) | DFS, BFS, recursion, level order | Binary tree helpers, Invert Binary Tree, List Of Depths, Maximum Depth, Validate BST, Is Subtree, First Common Ancestor, Binary Tree Level Order Traversal |
| Graphs | [`graphs`](graphs) | BFS, DFS, topological sort, Union Find | Graph search helpers, Route Between Nodes, Clone Graph, Build Order, Number Of Provinces, Redundant Connection, Number Of Islands |
| Heaps | [`heaps`](heaps) | min heap, top k, ranking | Min Heap, Kth Largest Element, Top K Frequent Elements, Relative Ranks, K Closest Points |
| Tries | [`tries`](tries) | prefixes, autocomplete, grid search | Trie implementation, Title Suggestions, Word Search |
| Sorting | [`sorting`](sorting) | comparison sort, divide and conquer | Bubble Sort, Selection Sort, Merge Sort, Quick Sort |
| Searching | [`searching`](searching) | binary search | Binary Search, Search Rotated Sorted Array |
| Dynamic programming | [`dynamic_programming`](dynamic_programming) | choose/skip, memoization, max/min subproblems | Robot In Grid, Set Subsets, Generate Parentheses, Maximum Subarray, Binary Tree Maximum Path Sum, Climbing Stairs |
| Bit manipulation | [`bit_manipulation`](bit_manipulation) | bits, masks, xor | Number Of One Bits, Reverse Integer, Number Conversion, Sum Integers |
| Extra problems | [`extra_problems`](extra_problems) | mixed interview patterns | Merge K Sorted Lists, Word Break, Reverse Nodes In K Group, Longest Unique Substring, House Robber, Coin Change |

See [`CONTRIBUTING.md`](CONTRIBUTING.md) to add problems. This repo uses the [`MIT License`](LICENSE).
