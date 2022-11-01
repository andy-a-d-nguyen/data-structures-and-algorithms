from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.node import Node


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.top = node
        else:
            node.next_node = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            popped_node = self.top
            self.top = self.top.next_node
            return popped_node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        return self.top is None
