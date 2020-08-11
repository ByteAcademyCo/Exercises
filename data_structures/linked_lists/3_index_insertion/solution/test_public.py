def test_solution():
    from solution import Node, linkedList

    items = linkedList()
    items.head = Node(20)
    items.head.next = Node(30)
    items.head.next.next = Node(40)
    items.insert_at_index(2, 2)

    assert items.head.data == 20
    assert items.head.next.data == 2
