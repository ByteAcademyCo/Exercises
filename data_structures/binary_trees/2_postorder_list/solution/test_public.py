def test_solution():
    from solution import Node, Postorder

    items = Node(5)
    items.left = Node(6)
    items.right = Node(7)
    items.left.left = Node(8)
    items.left.right = Node(9)
    result_value_1 = Postorder(items)
    result = [8, 9, 6, 7, 5]
    assert result_value_1 == result
