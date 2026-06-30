from typing import Optional
from ch06_Trees._00_binarytree.node import Node

class AncestorNode:
    def __init__(self):
        self.node_found = False
        self.ancestor = None

class FirstCommonAncestorSolution:
    def first_common_ancestor(self, root: Optional[Node], first_node: Optional[Node], second_node: Optional[Node]) -> Optional[Node]:
        return self._post_order_search(root, first_node, second_node).ancestor

    def _post_order_search(self, current: Optional[Node], first_node: Optional[Node], second_node: Optional[Node]) -> AncestorNode:
        if current is None:
            return AncestorNode()

        left_result = self._post_order_search(current.left, first_node, second_node)
        if left_result.ancestor is not None:
            return left_result

        right_result = self._post_order_search(current.right, first_node, second_node)
        if right_result.ancestor is not None:
            return right_result

        result = AncestorNode()
        if left_result.node_found and right_result.node_found:
            result.ancestor = current
            return result

        result.node_found = (current == first_node or
                             current == second_node or
                             left_result.node_found or
                             right_result.node_found)
        return result
