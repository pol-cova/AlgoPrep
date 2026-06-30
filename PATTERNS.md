# Patterns

Use this index to practice recognizing the underlying pattern before writing code.

## Arrays, Strings, and Hash Tables

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch03_ArraysStringsHashTables/_01_is_unique` | Set membership | duplicate detection, character scan |
| `ch03_ArraysStringsHashTables/_02_two_sum` | Hash map complement lookup | one-pass lookup, target sum |
| `ch03_ArraysStringsHashTables/_03_group_anagrams` | Frequency signature | grouping, normalized key |
| `ch03_ArraysStringsHashTables/_04_zero_matrix` | Matrix marking | in-place state, rows and columns |
| `ch14_ExtraProblems/_04_longest_unique_substring` | Sliding window | longest contiguous substring, uniqueness |

## Linked Lists

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch04_LinkedLists/_01_remove_dups` | Set membership | duplicate detection, pointer traversal |
| `ch04_LinkedLists/_02_merge__two_sorted_lists` | Two pointers | sorted inputs, merge step |
| `ch04_LinkedLists/_03_nth_node_to_last` | Fast and slow pointers | fixed gap, single pass |
| `ch04_LinkedLists/_04_add_two_numbers` | Carry simulation | digit-by-digit traversal |
| `ch04_LinkedLists/_05_swap_nodes_in_pairs` | Pointer rewiring | local linked-list mutation |
| `ch14_ExtraProblems/_01_merge_k_sorted_lists` | Heap merge | k sorted inputs, repeatedly choose minimum |
| `ch14_ExtraProblems/_03_reverse_nodes_kgroup` | Pointer rewiring | grouped reversal, fixed-size chunks |

## Stacks and Queues

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch05_StacksQueues/_01_queue_with_stacks` | Two-stack queue | amortized transfer |
| `ch05_StacksQueues/_02_valid_parenthesis` | Stack matching | nested delimiters |
| `ch05_StacksQueues/_03_sort_stack` | Auxiliary stack | constrained sorting |
| `ch05_StacksQueues/_04_stack_min` | Monotonic/min tracking | constant-time minimum |

## Trees

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch06_Trees/_01_invert_binary_tree` | DFS recursion | swap children |
| `ch06_Trees/_02_list_of_depths` | BFS by level | level grouping |
| `ch06_Trees/_03_maximum_depth` | DFS recursion | height aggregation |
| `ch06_Trees/_04_validate_bst` | DFS with bounds | ordered constraints |
| `ch06_Trees/_05_is_subtree` | Tree matching | recursive equality checks |
| `ch06_Trees/_06_first_common_ancestor` | LCA recursion | split paths |
| `ch12_DynamicProgramming/_05_binary_tree_max_path_sum` | Tree DP | best path through node |

## Graphs

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch07_Graphs/_01_route_between_nodes` | BFS/DFS reachability | path existence |
| `ch07_Graphs/_02_clone_graph` | DFS/BFS with visited map | copy graph, cycles |
| `ch07_Graphs/_03_build_order` | Topological sort | dependencies, ordering |
| `ch07_Graphs/_04_number_of_provinces` | Connected components | adjacency matrix |
| `ch07_Graphs/_05_redundant_connection` | Union find | cycle detection in undirected graph |

## Heaps and Priority Queues

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch08_Heaps/_00_min_heap` | Heap implementation | parent-child ordering |
| `ch08_Heaps/_01_kth_largest_element` | Heap selection | kth element |
| `ch08_Heaps/_02_top_k_frequent_elements` | Frequency map plus heap/bucket | top k by count |
| `ch08_Heaps/_03_relative_ranks` | Sorting or heap ranking | rank assignment |

## Tries

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch09_Tries/_00_trie` | Prefix tree | insert/search/prefix |
| `ch09_Tries/_01_title_suggestions` | Trie autocomplete | prefix suggestions |
| `ch09_Tries/_02_word_search` | Backtracking plus trie | grid search, shared prefixes |

## Sorting and Searching

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch10_Sorting/_00_sorting` | Sorting algorithms | compare and partition |
| `ch11_Searching/_00_binary_search` | Binary search | sorted input, monotonic condition |

## Dynamic Programming and Backtracking

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch12_DynamicProgramming/_01_robot_in_grid` | Grid DP/backtracking | path through obstacles |
| `ch12_DynamicProgramming/_02_set_subsets` | Backtracking | include/exclude choices |
| `ch12_DynamicProgramming/_03_generate_parenthesis` | Backtracking | constrained generation |
| `ch12_DynamicProgramming/_04_maximum_subarray` | Kadane's algorithm | best contiguous subarray |
| `ch14_ExtraProblems/_02_word_break` | DP over prefixes | dictionary segmentation |
| `ch14_ExtraProblems/_05_house_robber` | Linear DP | choose/skip adjacent items |
| `ch14_ExtraProblems/_06_coin_change` | Unbounded knapsack DP | minimum coins, repeated choices |

## Bit Manipulation

| Problem | Primary pattern | Secondary clues |
|---|---|---|
| `ch13_BitManipulation/_01_number_of_one_bits` | Bit counting | shift or clear lowest set bit |
| `ch13_BitManipulation/_02_reverse_int` | Digit simulation | overflow, sign handling |
| `ch13_BitManipulation/_03_number_conversion` | XOR difference | count changed bits |
| `ch13_BitManipulation/_04_sum_integers` | Bitwise addition | carry without `+` |
