class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"{{ {current.value} }} -> "
            current = current.next_node
        result += "NULL"
        return result

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next_node
        return False


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
