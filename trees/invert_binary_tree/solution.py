from typing import Optional
from trees.binary_tree.node import Node

class InvertBinaryTreeSolution:
    def invert_tree(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None

        # Swap left and right
        left = self.invert_tree(root.left)
        right = self.invert_tree(root.right)
        
        root.left = right
        root.right = left
        
        return root
