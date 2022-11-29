from data_structures.stack_and_queue.queue import Queue


def breadth_first(tree):
    if tree.root is None:
        return []
    else:
        result = []
        queue = Queue()
        queue.enqueue(tree.root)

        while queue.is_empty() is False:
            node = queue.dequeue()
            result.append(node.value)

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return result
