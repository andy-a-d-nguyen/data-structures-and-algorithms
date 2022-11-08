from data_structures.stack_and_queue.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, value):
        self.first_stack.push(value)

    def dequeue(self):
        while self.first_stack.is_empty() is False:
            popped_value = self.first_stack.pop()
            self.second_stack.push(popped_value)
        oldest_value = self.second_stack.pop()
        while self.second_stack.is_empty() is False:
            popped_value = self.second_stack.pop()
            self.first_stack.push(popped_value)
        return oldest_value
