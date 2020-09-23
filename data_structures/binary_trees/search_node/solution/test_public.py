def test_solution():
    from solution import Node, search

    items = Node(5)
    items.left = Node(6)
    items.right = Node(7)
    items.left.left = Node(8)
    items.left.right = Node(9)
    items.right.left = Node(10)
    items.right.right = Node(11)
    result_value = search(items, 11)
    result_value_2 = search(items, 99)
    assert result_value == True
    assert result_value_2 == False
