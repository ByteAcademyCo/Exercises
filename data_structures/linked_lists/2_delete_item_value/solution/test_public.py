def test_solution():
    from solution import Node, linkedList

    items = linkedList()
    items.head = Node(20)
    items.head.next = Node(30)
    items.head.next.next = Node(40)
    items.head.next.next.next = Node(50)
    items.delete_item_by_value(40)

    assert items.head.data == 20
    assert items.head.next.data == 30
    assert items.head.next.next.data == 50
