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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def insert_before(self, value_to_find, value_to_insert):
        node_to_insert = Node(value_to_insert)
        if self.head is None or self.includes(value_to_find) is False:
            raise TargetError
        elif self.head.next_node is None:
            node_to_insert.next_node = self.head
            self.head = node_to_insert
        else:
            current = self.head
            while current.next_node is not None:
                if current.next_node.value == value_to_find:
                    node_to_insert.next_node = current.next_node
                    current.next_node = node_to_insert
                    break
                else:
                    current = current.next_node

    def insert_after(self, value_to_find, value_to_insert):
        if self.head is None or self.includes(value_to_find) is False:
            raise TargetError
        else:
            current = self.head
            while current is not None:
                if current.value == value_to_find:
                    node_to_insert = Node(value_to_insert)
                    node_to_insert.next_node = current.next_node
                    current.next_node = node_to_insert
                    break
                else:
                    current = current.next_node


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class TargetError(Exception):
    pass
