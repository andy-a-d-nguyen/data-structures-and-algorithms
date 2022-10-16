from data_structures.doubly_linked_list.doubly_linked_list import DoublyLinkedList, Node


def test_node():
    node = Node(10, None, None)
    assert node.value == 10
    assert node.previous_node is None
    assert node.next_node is None


def test_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    assert doubly_linked_list is not None
    assert doubly_linked_list.head is None


def test_insert():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(20)
    assert doubly_linked_list.head.value == 20
    assert doubly_linked_list.head.previous_node is None
    assert doubly_linked_list.head.next_node is None
    doubly_linked_list.insert(30)
    assert doubly_linked_list.head.value == 30
    assert doubly_linked_list.head.previous_node is None
    assert doubly_linked_list.head.next_node.value == 20
    assert doubly_linked_list.head.next_node.previous_node.value == 30


def test_includes():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(20)
    doubly_linked_list.insert(30)
    doubly_linked_list.insert(40)
    assert doubly_linked_list.includes(20) is True
    assert doubly_linked_list.includes(50) is False


def test_to_string():
    doubly_linked_list = DoublyLinkedList()
    assert str(doubly_linked_list) == "NULL"
    doubly_linked_list.insert(20)
    doubly_linked_list.insert(30)
    doubly_linked_list.insert(40)
    assert str(doubly_linked_list) == "{ 40 } -> { 30 } -> { 20 } -> NULL"
