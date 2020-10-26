def test_solution():
    import solution
    
    tasks1 = [(14, 15), (8, 13), (9, 11), (11, 13), (14, 16)]
    tasks2 = [(9, 17), (9,12), (13, 17)]
    tasks3 = [(9, 17), (10,17), (13, 17)]
    tasks4 = [(10, 15), (10,17), (10, 13)]

    assert solution.task_schedule(tasks1) == 3
    assert solution.task_schedule([]) == 0
    assert solution.task_schedule([(9, 17)]) == 1
    assert solution.task_schedule(tasks2) == 2
    assert solution.task_schedule(tasks3) == 1
    assert solution.task_schedule(tasks4) == 1