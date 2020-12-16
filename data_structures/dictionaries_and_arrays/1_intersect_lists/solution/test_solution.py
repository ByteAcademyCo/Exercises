def test_solution():
    from solution import intersect_lists

    lst1 = [1, "a", -2, 1.4]
    lst2 = ["cat", 0.5, "a", 1, 2]

    ret_lst = intersect_lists(lst1, lst2)

    ret_lst2 = intersect_lists(["a", "b"], ["b", "a"])

    assert (ret_lst == ["a", 1] or ret_lst == [1, "a"]) == True
    assert intersect_lists([1, 2, 3], [4, 5]) == []
    assert intersect_lists([], []) == []
    assert (ret_lst2 == ["a", "b"] or ret_lst2 == ["b", "a"]) == True
