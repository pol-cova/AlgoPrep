import pytest
from trees.binary_tree.node import Node
from trees.validate_bst.validate_bst import ValidateBST
from trees.validate_bst.solution import ValidateBSTSolution

@pytest.mark.parametrize("klass", [ValidateBST, ValidateBSTSolution])
def test_validate_bst(klass):
    instance = klass()
    try:
        # Invalid BST
        root_invalid = Node(4)
        root_invalid.left = Node(5)
        root_invalid.right = Node(7)
        root_invalid.left.left = Node(1)
        root_invalid.left.right = Node(3)
        root_invalid.left.left.left = Node(8)
        
        assert instance.is_valid_bst(root_invalid) is False

        # Valid BST
        root_valid = Node(4)
        root_valid.left = Node(2)
        root_valid.right = Node(7)
        root_valid.left.left = Node(1)
        root_valid.left.right = Node(3)
        root_valid.right.left = Node(5)
        
        assert instance.is_valid_bst(root_valid) is True
    except NotImplementedError:
        pytest.skip("ValidateBST is not implemented yet")
