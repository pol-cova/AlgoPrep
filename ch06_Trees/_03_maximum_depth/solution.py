from typing import Optional
from ch06_Trees._00_binarytree.node import Node

class MaximumDepthSolution:
    def max_depth(self, root: Optional[Node]) -> int:
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
