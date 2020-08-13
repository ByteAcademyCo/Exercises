def test_solution():
    from solution import Node, closest_value

    root = Node(8)
    root.left = Node(5)
    root.right = Node(14)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.left.right.left = Node(8)
    root.left.right.right = Node(7)
    root.right.right = Node(24)
    root.right.right.left = Node(22)
    result = closest_value(root, 9)
    assert result == 8
