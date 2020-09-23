def test_solution():
    import solution
    
    assert solution.knap_sack(5, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}) == 8
    assert solution.knap_sack(5, {}) == 0
    assert solution.knap_sack(0, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}) == 0
    assert solution.knap_sack(5, {"hat": (2,2), "sunscreen": (3,2), "food": (4,4)}) == 5