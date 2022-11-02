from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.node import Node


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None):
        self.front = front
        self.back = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.back = node
        else:
            current = self.front
            while current.next_node is not None:
                current = current.next_node
            current.next_node = node
            self.back = node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            dequeued_node = self.front
            self.front = self.front.next_node
            return dequeued_node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.front.value

    def is_empty(self):
        return self.front is None

