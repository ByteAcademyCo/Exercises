def test_solution():
    import solution

    sib_dict1 = {"Anton": 10,
                "Cosette": 3,
                "Nancy": 15,
                "Lucas": 15}
    ret1 = [("Cosette", 3), ("Anton", 10), ("Lucas", 15), ("Nancy", 15)]

    sib_dict2 = {"Sara": 15,
                "Reena": 15,
                "Alex": 15,
                "Justin": 15}
    ret2 = [("Alex", 15), ("Justin", 15), ("Reena", 15), ("Sara", 15)]

    assert solution.sort_siblings(sib_dict1) == ret1
    assert solution.sort_siblings({}) == []
    assert solution.sort_siblings({"Anton": 10}) == [("Anton", 10)]
    assert solution.sort_siblings(sib_dict2) == ret2
