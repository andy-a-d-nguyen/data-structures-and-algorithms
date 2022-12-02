from data_structures.kary_tree import KaryTree, Node
from data_structures.stack_and_queue.queue import Queue


def fizz_buzz_tree(tree):
    queue = Queue()
    new_tree = KaryTree(clone_tree(tree.root))
    queue.enqueue(new_tree.root)

    while queue.is_empty() is False:
        node = queue.dequeue()
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for child in node.children:
            queue.enqueue(child)

    return new_tree


def fizz_buzz_tree_recursive(tree):
    new_tree = KaryTree(clone_tree(tree.root))
    if new_tree.root is None:
        return
    else:
        new_tree.root = fizz_buzz_tree_helper(new_tree.root)
        return new_tree


def fizz_buzz_tree_helper(node):
    if node is None:
        return
    else:
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for child in node.children:
            fizz_buzz_tree_helper(child)

        return node


def clone_tree(node):
    if node is None:
        return
    else:
        new_node = Node(node.value)
        for child in node.children:
            new_child = clone_tree(child)
            new_node.children.append(new_child)
        return new_node
