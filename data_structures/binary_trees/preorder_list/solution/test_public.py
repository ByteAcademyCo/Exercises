def test_solution():
    from solution import Node, Preorder

    items = Node(5)
    items.left = Node(6)
    items.right = Node(7)
    items.left.left = Node(8)
    items.left.right = Node(9)
    result_value_1 = Preorder(items)
    result = [5, 6, 8, 9, 7]
    assert result_value_1 == result
