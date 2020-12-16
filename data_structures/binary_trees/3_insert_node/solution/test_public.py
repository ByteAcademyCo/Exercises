def test_solution():
    from solution import Node

    items = Node(10)
    items.left = Node(11)
    items.left.left = Node(7)
    items.right = Node(9)
    items.right.left = Node(15)
    items.right.right = Node(8)
    val = 12
    items.insert(val)
    assert items.left.right.key == 12
