def task_schedule(tasks):
    # sort the tasks list by finishing time.
    tasks.sort(key = lambda t: t[1])
    num_tasks = 0
    cur_end = 0
    # itterate through the tasks
    for t in tasks:
        # if task ts start time is later or equal to our current end time
        # we can do that task, so we update the end time to ts end time and
        # increment the number of tasks by 1.
        if t[0] >= cur_end:
            cur_end = t[1]
            num_tasks += 1
    # once we've itterated through all the tasks we return the num_tasks
    # we could complete.
    return num_tasks