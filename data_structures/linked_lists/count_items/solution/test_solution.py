def test_solution():
    from solution_3 import Node, linkedList

    items = linkedList()
    items.head = Node(20)
    items.head.next = Node(30)
    items.head.next.next = Node(40)

    assert items.get_count() == 3
