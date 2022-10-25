from data_structures.linked_list.linked_list import LinkedList


def zip_lists(a, b):
    result = LinkedList()
    if a.head is None and b.head is not None:
        result.head = b.head
        return result
    elif b.head is None and a.head is not None:
        result.head = a.head
        return result

    a_current = a.head
    a_next = a_current.next_node
    b_current = b.head
    b_next = b_current.next_node
    result.head = a_current

    while a_next is not None or b_next is not None:
        # zipping nodes
        if b_current is not None:
            if a_current is not None:
                a_current.next_node = b_current
        if a_next is not None:
            if b_current is not None:
                b_current.next_node = a_next

        # moving currents and nexts forward
        a_current = a_next
        if a_next is not None:
            a_next = a_next.next_node
        b_current = b_next
        if b_next is not None:
            b_next = b_next.next_node

    if b_current is not None:
        if a_current is not None:
            a_current.next_node = b_current

    return result
