def test_solution():
    from solution import inorder_to_postorder

    assert inorder_to_postorder("1+2+3") == "123++"
    assert inorder_to_postorder("1+2*3-4/2") == "12342+*-/"
    assert inorder_to_postorder("1") == "1"
    assert inorder_to_postorder("") == ""