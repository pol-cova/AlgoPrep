from typing import Optional
from ch12_DynamicProgramming._05_binary_tree_max_path_sum.tree_node import TreeNode

class BinaryTreeMaxPathSumSolution:
    def __init__(self):
        self.max_sum = -2147483648

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -2147483648
        self._max_path_sum_helper(root)
        return self.max_sum

    def _max_path_sum_helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = max(self._max_path_sum_helper(root.left), 0)
        right = max(self._max_path_sum_helper(root.right), 0)

        self.max_sum = max(self.max_sum, root.val + left + right)

        return root.val + max(left, right)
