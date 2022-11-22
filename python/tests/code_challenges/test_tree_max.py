import pytest
from data_structures.binary_tree_and_BST.binary_tree import BinaryTree
from data_structures.binary_tree_and_BST.tree_node import Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_find_maximum_value_no_root():
    tree = BinaryTree()
    assert tree.find_maximum_value() is None


def test_find_maximum_value_numeric():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    assert tree.find_maximum_value() == 11


def test_find_maximum_value_non_numeric():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node('7')
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node('6')
    tree.root.left.right.left = Node(5.5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node('four')
    assert tree.find_maximum_value() == 11
