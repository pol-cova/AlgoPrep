# Patterns

Use this before coding. Read the problem, guess the pattern, then implement.

## Quick Cues

| If the prompt says... | Try... |
|---|---|
| sorted input | binary search or two pointers |
| pair, target, complement | hash map |
| longest/shortest contiguous range | sliding window |
| counts, duplicates, groups | hash map or frequency map |
| nested or matching items | stack |
| top k or kth largest/smallest | heap |
| tree height, path, ancestor | DFS |
| levels or shortest unweighted path | BFS |
| connected components | DFS, BFS, or Union Find |
| dependencies or ordering | topological sort |
| all subsets, combos, permutations | backtracking |
| best/min/max after choices | dynamic programming |
| prefixes or autocomplete | trie |
| bits, xor, no arithmetic | bit manipulation |

## Common Patterns

- **Hash map**: fast lookup, counts, duplicates, complements.
- **Two pointers**: sorted input, merging, pair search, linked-list gaps.
- **Sliding window**: contiguous subarray or substring with a moving condition.
- **Stack**: most recent unresolved item matters.
- **BFS**: level order or shortest path in an unweighted graph.
- **DFS**: explore branches, trees, components, or paths.
- **Backtracking**: generate all valid answers.
- **Dynamic programming**: repeated subproblems with choose/skip or min/max decisions.
- **Heap**: repeatedly need the current smallest/largest.
- **Union Find**: merge groups and ask whether items are connected.

## Problems By Pattern

### Hash Map / Set

- `ch03_ArraysStringsHashTables/_01_is_unique`
- `ch03_ArraysStringsHashTables/_02_two_sum`
- `ch03_ArraysStringsHashTables/_03_group_anagrams`
- `ch04_LinkedLists/_01_remove_dups`

### Two Pointers / Linked Lists

- `ch04_LinkedLists/_02_merge__two_sorted_lists`
- `ch04_LinkedLists/_03_nth_node_to_last`
- `ch04_LinkedLists/_04_add_two_numbers`
- `ch04_LinkedLists/_05_swap_nodes_in_pairs`
- `ch14_ExtraProblems/_03_reverse_nodes_kgroup`

### Sliding Window

- `ch14_ExtraProblems/_04_longest_unique_substring`

### Stack / Queue

- `ch05_StacksQueues/_01_queue_with_stacks`
- `ch05_StacksQueues/_02_valid_parenthesis`
- `ch05_StacksQueues/_03_sort_stack`
- `ch05_StacksQueues/_04_stack_min`

### Trees

- `ch06_Trees/_01_invert_binary_tree`
- `ch06_Trees/_02_list_of_depths`
- `ch06_Trees/_03_maximum_depth`
- `ch06_Trees/_04_validate_bst`
- `ch06_Trees/_05_is_subtree`
- `ch06_Trees/_06_first_common_ancestor`
- `ch12_DynamicProgramming/_05_binary_tree_max_path_sum`

### Graphs

- `ch07_Graphs/_01_route_between_nodes`
- `ch07_Graphs/_02_clone_graph`
- `ch07_Graphs/_03_build_order`
- `ch07_Graphs/_04_number_of_provinces`
- `ch07_Graphs/_05_redundant_connection`

### Heap

- `ch08_Heaps/_00_min_heap`
- `ch08_Heaps/_01_kth_largest_element`
- `ch08_Heaps/_02_top_k_frequent_elements`
- `ch08_Heaps/_03_relative_ranks`
- `ch14_ExtraProblems/_01_merge_k_sorted_lists`

### Trie

- `ch09_Tries/_00_trie`
- `ch09_Tries/_01_title_suggestions`
- `ch09_Tries/_02_word_search`

### Search / Sort

- `ch10_Sorting/_00_sorting`
- `ch11_Searching/_00_binary_search`

### Backtracking / Dynamic Programming

- `ch12_DynamicProgramming/_01_robot_in_grid`
- `ch12_DynamicProgramming/_02_set_subsets`
- `ch12_DynamicProgramming/_03_generate_parenthesis`
- `ch12_DynamicProgramming/_04_maximum_subarray`
- `ch14_ExtraProblems/_02_word_break`
- `ch14_ExtraProblems/_05_house_robber`
- `ch14_ExtraProblems/_06_coin_change`

### Bit Manipulation

- `ch13_BitManipulation/_01_number_of_one_bits`
- `ch13_BitManipulation/_02_reverse_int`
- `ch13_BitManipulation/_03_number_conversion`
- `ch13_BitManipulation/_04_sum_integers`
