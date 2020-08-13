def test_solution():
    from solution import Node, NthPreorder

    items = Node(25)
    items.left = Node(20)
    items.right = Node(30)
    items.left.left = Node(18)
    items.left.right = Node(22)
    items.right.left = Node(24)
    items.right.right = Node(32)
 
    assert NthPreorder(items, 6) == 24
    assert NthPreorder(items, 4) == 22
    assert NthPreorder(items, 8) == "no 8-th element"