def test_solution():
    from solution import Node, linkedlist

    items = linkedlist()
    items.head = Node(20)
    items.head.next = Node(30)
    items.head.next.next = Node(50)
    print(items.head, items.head.next, items.head.next.next)
    items.delete_at_end()
    assert items.head.data == 20
    assert items.head.next.data == 30
    assert items.head.next.next == None