class Node:
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"{{ {current.value} }} -> "
            current = current.next_node
        result += "NULL"
        return result

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.head.previous_node = node
            node.next_node = self.head
            self.head = node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next_node
        return False
