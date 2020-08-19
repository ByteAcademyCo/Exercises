def max_profits(projects):
    projects.sort(key = lambda x: x[1], reverse=True)
    dict = {}
    profit = 0
    for x in projects:
        for i in range(x[0], 0, -1):
            if not i in dict:
                dict[i] = x[1]
                profit += x[1]
                break
    return profit