def test_solution():
    from solution import Node, linkedList

    items = linkedList()
    items.head = Node(20)
    items.head.next = Node(30)
    items.head.next.next = Node(40)
    items.reverse()

    assert items.head.data == 40
    assert items.head.next.data == 30
