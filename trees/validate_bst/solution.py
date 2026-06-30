from typing import Optional
from trees.binary_tree.node import Node

class ValidateBSTSolution:
    def is_valid_bst(self, root: Optional[Node]) -> bool:
        return self._is_valid_bst_helper(root, None, None)

    def _is_valid_bst_helper(self, root: Optional[Node], min_val: Optional[int], max_val: Optional[int]) -> bool:
        if root is None:
            return True
        if (min_val is not None and root.value <= min_val) or (max_val is not None and root.value >= max_val):
            return False

        return (self._is_valid_bst_helper(root.left, min_val, root.value) and
                self._is_valid_bst_helper(root.right, root.value, max_val))
