def max_profits(projects):
    # sort projects by max_profit
    projects.sort(key = lambda t: t[1], reverse=True)
    project_dict = {}
    total_profit = 0
    for p in projects:
        for i in range(p[0],0, -1):
            # add project p to latest time slot it can be added
            # to in project dict without an existing project
            if not i in project_dict:
                project_dict[i] = p[1]
                total_profit += p[1]
                break
    return total_profit

projects = [(1, 100), (2, 150), (2, 300), (4, 200), (3, 100)]
print(max_profits(projects))
