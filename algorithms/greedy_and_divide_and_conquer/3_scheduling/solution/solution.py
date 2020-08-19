
def task_schedule(tasks):
    tasks.sort(key = lambda x: x[1])
    number_of_tasks = 0
    current_end = 0
    for x in tasks:
        if x[0] >= current_end:
            current_end = x[1]
            number_of_tasks += 1
    return number_of_tasks