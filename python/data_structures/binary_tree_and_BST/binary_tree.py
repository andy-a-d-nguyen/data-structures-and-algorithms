import math

from data_structures.binary_tree_and_BST.tree_node import Node


class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        result = []
        pre_order_helper(self.root, result)
        return result

    def in_order(self):
        result = []
        in_order_helper(self.root, result)
        return result

    def post_order(self):
        result = []
        post_order_helper(self.root, result)
        return result

    def find_maximum_value(self):
        if self.root is None:
            return None
        else:
            # return find_max_value_helper_numeric_only(self.root, float('-inf'))
            max_value = float('-inf')
            values = []
            find_max_value_helper(self.root, values)
            for value in values:
                try:
                    if value > max_value:
                        max_value = value
                except Exception:
                    continue
            return max_value


def pre_order_helper(root, result):
    if root is None:
        return
    else:
        result.append(root.value)
        pre_order_helper(root.left, result)
        pre_order_helper(root.right, result)


def in_order_helper(root, result):
    if root is None:
        return
    else:
        in_order_helper(root.left, result)
        result.append(root.value)
        in_order_helper(root.right, result)


def post_order_helper(root, result):
    if root is None:
        return
    else:
        post_order_helper(root.left, result)
        post_order_helper(root.right, result)
        result.append(root.value)


def find_max_value_helper(node, values):
    if node is None:
        return
    else:
        values.append(node.value)
        find_max_value_helper(node.left, values)
        find_max_value_helper(node.right, values)


def find_max_value_helper_numeric_only(node, max_value):
    # Base case
    # node has no children
    current_max = max_value
    if node.left is None and node.right is None:
        if node.value > current_max:
            current_max = node.value
    # Recursive case
    # node has children
    else:
        left = max_value
        right = max_value
        if node.left is not None:
            left = find_max_value_helper_numeric_only(node.left, current_max)
        if node.right is not None:
            right = find_max_value_helper_numeric_only(node.right, current_max)

        if node.value > left and node.value > right:
            current_max = node.value
        elif left > node.value and left > right:
            current_max = left
        elif right > node.value and right > left:
            current_max = right
    return current_max
