def test_solution():
    from solution import Node, linkedList

    items = linkedList()
    items.head = Node(20)
    items.insert_at_start(40)
    items.insert_at_start(50)
    assert items.head.data == 50
    assert items.head.next.data == 40
    assert items.head.next.next.data == 20
