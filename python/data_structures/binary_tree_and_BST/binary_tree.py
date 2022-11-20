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
