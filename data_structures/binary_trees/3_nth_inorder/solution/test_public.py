def test_solution():
    from solution import Node, NthInorder

    items = Node(5)
    items.left = Node(6)
    items.right = Node(7)
    items.left.left = Node(8)
    items.left.right = Node(9)

    [8, 6, 9, 5, 7]

    assert NthInorder(items, 4) == 5
    assert NthInorder(items, 1) == 8
    assert NthInorder(items, 6) == "no 6-th element"