from ch06_Trees._00_binarytree.node import Node

class BinaryTreeTraversals:
    @staticmethod
    def in_order_traversal(node: Node) -> None:
        if node is not None:
            BinaryTreeTraversals.in_order_traversal(node.left)
            print(node.value, end=" ")
            BinaryTreeTraversals.in_order_traversal(node.right)

    @staticmethod
    def pre_order_traversal(node: Node) -> None:
        if node is not None:
            print(node.value, end=" ")
            BinaryTreeTraversals.pre_order_traversal(node.left)
            BinaryTreeTraversals.pre_order_traversal(node.right)

    @staticmethod
    def post_order_traversal(node: Node) -> None:
        if node is not None:
            BinaryTreeTraversals.post_order_traversal(node.left)
            BinaryTreeTraversals.post_order_traversal(node.right)
            print(node.value, end=" ")
