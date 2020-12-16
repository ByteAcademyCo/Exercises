def test_solution():
    from solution import Node, height

    left_child = Node(6, None, None)
    right_child = Node(7, None, None)
    items = Node(5, left_child, right_child)
    items.left.left = Node(8)
    items.left.right = Node(9)
    items.right.left = Node(10)
    result = height(items)
    assert result == 3
