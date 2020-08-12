import solution

queue1 = solution.Queue()
queue1.enqueue(1)
queue1.enqueue(2)

queue2 = solution.Queue()


def test_solution():
    assert bool(queue1) == True
    assert bool(queue2) == False
