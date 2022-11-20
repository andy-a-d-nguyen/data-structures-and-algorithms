import pytest
from data_structures.binary_tree_and_BST.binary_tree import BinaryTree
from data_structures.binary_tree_and_BST.tree_node import Node


@pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected
