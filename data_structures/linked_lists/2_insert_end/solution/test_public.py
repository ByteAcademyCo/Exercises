def test_solution():
    from solution import Node, linkedList

    items = linkedList()
    items.head = Node(20)
    items.head.next = Node(30)
    items.insert_at_end(40)

    assert items.head.data == 20
    assert items.head.next.data == 30
    assert items.head.next.next.data == 40
