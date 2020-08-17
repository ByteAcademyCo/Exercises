def task_schedule(tasks):
    tasks.sort(key = lambda t: t[1])
    num_tasks = 0
    #cur_start = tasks[0][0]
    cur_end = 0
    for t in tasks:
        if t[0] >= cur_end:
            cur_end = t[1]
            num_tasks += 1
    return num_tasks


tasks = [(14, 15), (8, 13), (9, 11), (11, 13), (14, 16)]
print(task_schedule(tasks))