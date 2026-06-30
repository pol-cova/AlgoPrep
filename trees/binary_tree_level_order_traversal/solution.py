from collections import deque
from typing import List, Optional
from trees.binary_tree.node import Node

class BinaryTreeLevelOrderTraversalSolution:
    def level_order(self, root: Optional[Node]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.value)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)

        return result
