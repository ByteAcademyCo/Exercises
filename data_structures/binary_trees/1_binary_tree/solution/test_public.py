def test_solution():
    from solution import sample_tree

    assert sample_tree.key == 5
    assert sample_tree.left.key == 4
    assert sample_tree.right.key == 7
