# Interview Pattern Recognition

Before coding, classify the problem. The faster you identify the pattern, the easier it is to choose data structures and edge cases.

## Quick Cues

| Clue in the prompt | Consider |
|---|---|
| "sorted array", "sorted list" | Binary search, two pointers, merge |
| "find pair", "target sum", "complement" | Hash map, two pointers if sorted |
| "longest/shortest contiguous subarray" | Sliding window, prefix sum |
| "subarray sum equals k" | Prefix sum plus hash map |
| "top k", "kth largest", "smallest k" | Heap, quickselect, bucket count |
| "group by same letters/counts" | Hash map with normalized key |
| "valid parentheses", "next greater" | Stack |
| "minimum/maximum at every step" | Heap, monotonic stack, monotonic queue |
| "all combinations/permutations/subsets" | Backtracking |
| "grid path", "island", "connected region" | DFS/BFS, Union Find |
| "dependencies", "course schedule", "build order" | Topological sort |
| "shortest path in unweighted graph" | BFS |
| "tree height/path/ancestor" | DFS recursion |
| "prefix", "autocomplete", "dictionary search" | Trie |
| "choose or skip", "optimal substructure" | Dynamic programming |
| "cannot rob adjacent", "climb stairs" | Linear DP |
| "change amount", "minimum coins" | Knapsack-style DP |
| "set bits", "xor", "without arithmetic operators" | Bit manipulation |

## Pattern Checklist

Ask these in order:

1. Is the input sorted or monotonic?
2. Does the answer depend on a contiguous window?
3. Do I need fast lookup of a previously seen value?
4. Does the problem ask for all valid choices?
5. Can the problem be modeled as a graph?
6. Is there repeated work with an optimal subproblem?
7. Is `k` central to the problem?
8. Are prefixes or word lookups involved?

## Common Pattern Notes

### Hash Map

Use when you need constant-time lookup by value, frequency, complement, or previously seen state.

Typical signals:

- duplicates
- counts
- grouping
- target/complement
- first index of a prefix value

### Two Pointers

Use when you can move inward or forward based on a comparison.

Typical signals:

- sorted input
- pair search
- merging sorted sequences
- removing duplicates in place

### Sliding Window

Use for contiguous ranges where expanding and shrinking a window preserves a useful invariant.

Typical signals:

- longest substring
- shortest subarray
- at most / at least constraints
- contiguous sequence

### Stack

Use when the most recent unresolved item must be handled first.

Typical signals:

- nested structure
- matching pairs
- previous greater/smaller element
- undo-like behavior

### BFS

Use when exploring by distance or level.

Typical signals:

- shortest path in an unweighted graph
- tree levels
- minimum number of moves

### DFS

Use when exploring full branches or recursive structure.

Typical signals:

- tree recursion
- connected components
- path existence
- backtracking search

### Dynamic Programming

Use when brute force repeats the same subproblems and choices can be cached.

Typical signals:

- count ways
- min/max cost
- choose/skip
- prefixes
- grid paths

### Backtracking

Use when you need to enumerate valid configurations.

Typical signals:

- all subsets
- all permutations
- all combinations
- valid generated strings
- board/grid search

### Heap

Use when you repeatedly need the current min or max.

Typical signals:

- top k
- kth largest/smallest
- merge k sorted lists
- streaming rank

### Union Find

Use when you need to merge groups and query connectivity.

Typical signals:

- connected components
- redundant connection
- cycle in undirected graph
- accounts/groups merging
