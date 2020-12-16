def test_solution():
    import solution

    queue1 = solution.Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)

    queue2 = solution.Queue()
    queue2.enqueue(1)

    queue3 = solution.Queue()
    queue3.enqueue(1)
    
    assert (queue1 == queue2) == False
    assert (queue2 == queue3) == True
    assert (queue3 == queue1) == False