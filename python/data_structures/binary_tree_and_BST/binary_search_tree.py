from data_structures.binary_tree_and_BST.binary_tree import BinaryTree
from data_structures.binary_tree_and_BST.tree_node import Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        super().__init__()

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            add_helper(self.root, value)

    def contains(self, value):
        return contains_helper(self.root, value)


def add_helper(node, value):
    # Base Case:
    # node has no left child or right child or both
    if node.left is None or node.right is None:
        if value < node.value:
            node.left = Node(value)
        elif value > node.value:
            node.right = Node(value)
    # Recursive Case:
    # node has children
    else:
        if value < node.left.value:
            add_helper(node.left, value)
        elif value > node.right.value:
            add_helper(node.right, value)


def contains_helper(node, value):
    # Base case
    # node with no children
    if node.left is None and node.right is None:
        if value == node.value:
            return True
        else:
            return False
    # Recursive case
    # node with children
    else:
        if value < node.value:
            return contains_helper(node.left, value)
        elif value > node.value:
            return contains_helper(node.right, value)
