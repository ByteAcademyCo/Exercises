def test_solution():
    import solution

    queue1 = solution.Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    queue1.enqueue(5)

    queue2 = solution.Queue()
    queue2.enqueue(2)

    queue3 = solution.Queue()
    
    assert len(queue1) == 5
    assert len(queue2) == 1
    assert len(queue3) == 0