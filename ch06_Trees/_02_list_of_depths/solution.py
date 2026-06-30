from typing import List, Optional
from ch06_Trees._00_binarytree.node import Node

class ListOfDepthsSolution:
    def list_of_depths(self, root: Optional[Node]) -> Optional[List[List[Node]]]:
        if root is None:
            return None

        result = []
        current = [root]

        while current:
            result.append(current)
            parents = current
            current = []
            for node in parents:
                if node.left is not None:
                    current.append(node.left)
                if node.right is not None:
                    current.append(node.right)
                    
        return result
