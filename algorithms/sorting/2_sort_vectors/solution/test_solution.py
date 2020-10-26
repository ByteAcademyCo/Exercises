

def test_solution():
    import solution

    vects1 = [((1, 3), (2, 6)), ((1, 5), (3, 4)), ((2, 6), (2, 9))]
    ret1 = [((1, 5), (3, 4)), ((2, 6), (2, 9)), ((1, 3), (2, 6))]

    vects2 = [((2, 6), (2, 9)), ((1, 3), (2, 6))] #sorted order

    vects3 = [((1, 8), (2, 4))]
    
    assert solution.sort_vectors(vects1) == ret1
    assert solution.sort_vectors([]) == []
    assert solution.sort_vectors(vects2) == vects2
    assert solution.sort_vectors(vects3) == vects3
    
