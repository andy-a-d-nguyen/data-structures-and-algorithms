import pytest
from data_structures.binary_tree_and_BST.binary_tree import BinaryTree
from data_structures.binary_tree_and_BST.tree_node import Node


# @pytest.mark.skip("TODO")
def test_exists():
    assert BinaryTree


# @pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


def test_empty_tree():
    tree = BinaryTree()
    assert tree.root is None


def test_tree_single_root_node():
    tree = BinaryTree()
    tree.root = Node(1, Node(2), Node(3))
    assert tree.root.value == 1
    assert tree.root.left.value == 2
    assert tree.root.left.left is None
    assert tree.root.left.right is None
    assert tree.root.right.value == 3
    assert tree.root.right.left is None
    assert tree.root.right.right is None


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree
