from typing import Optional
from trees.binary_tree.node import Node

class IsSubTreeSolution:
    def is_subtree(self, first: Optional[Node], second: Optional[Node]) -> bool:
        stb1 = []
        stb2 = []
        self._pre_order(first, stb1)
        self._pre_order(second, stb2)
        
        str1 = ",".join(stb1)
        str2 = ",".join(stb2)
        return str2 in str1

    def _pre_order(self, node: Optional[Node], stb: list) -> None:
        if node is None:
            stb.append("X")
            return
        stb.append(str(node.value))
        self._pre_order(node.left, stb)
        self._pre_order(node.right, stb)
