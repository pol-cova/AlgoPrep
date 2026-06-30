import pytest
from ch12_DynamicProgramming._05_binary_tree_max_path_sum.tree_node import TreeNode
from ch12_DynamicProgramming._05_binary_tree_max_path_sum.binary_tree_max_path_sum import BinaryTreeMaxPathSum
from ch12_DynamicProgramming._05_binary_tree_max_path_sum.solution import BinaryTreeMaxPathSumSolution

@pytest.mark.parametrize("klass", [BinaryTreeMaxPathSum, BinaryTreeMaxPathSumSolution])
def test_binary_tree_max_path_sum(klass):
    instance = klass()
    try:
        # Example 1
        root1 = TreeNode(2)
        root1.left = TreeNode(1)
        root1.right = TreeNode(3)
        root1.left.left = TreeNode(-5)
        root1.right.right = TreeNode(-1)

        assert instance.max_path_sum(root1) == 6

        # Example 2
        root2 = TreeNode(-12)
        root2.left = TreeNode(5)
        root2.right = TreeNode(3)
        root2.right.left = TreeNode(1)
        root2.right.right = TreeNode(4)

        assert instance.max_path_sum(root2) == 8
    except NotImplementedError:
        pytest.skip("BinaryTreeMaxPathSum is not implemented yet")
