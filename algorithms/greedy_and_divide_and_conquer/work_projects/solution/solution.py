def max_profits(projects):
    # sort list of project tuples by highest profit
    projects.sort(key = lambda t: t[1], reverse=True)
    project_dict = {}
    total_profit = 0
    # itterate through the list of projects
    for p in projects:
        # itterare through the possible time slots you can complete 
        # that project in starting at the latest time slot.
        for i in range(p[0],0, -1):
            # add project p to latest time slot it can be added
            # to in project dict without an existing project
            if not i in project_dict:
                # add this project to our project dict.
                project_dict[i] = p[1]
                # update total_profit 
                total_profit += p[1]
                # break out of inner loop if we've added the project
                break
    # return total_profit once we've added all the projects we can.
    return total_profit