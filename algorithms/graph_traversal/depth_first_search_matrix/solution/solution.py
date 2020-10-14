# Depth First Search Solution
def exists_path(matrix, origin, destination):
    def exists_path_visited(matrix, origin, destination, visited):
        if origin in visited:
            return False
        if not (origin in range(len(matrix)) and 
                destination in range(len(matrix))):
                return False
        elif matrix[origin][destination] == 1:
            return True
        visited.append(origin)
        for j in range(len(matrix[origin])):
            if matrix[origin][j] == 1 and exists_path_visited(matrix, j, destination, visited):
                return True
        return False
    return exists_path_visited(matrix, origin, destination, [])


# Ineficient Solution
def reachable_dict(matrix):
    reachable_dict = {}
    for i in range(len(matrix)):
        reachable_lst = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                reachable_lst.append(j)
        reachable_dict[i] = reachable_lst
    all_reachable = {}
    for i, neighbours in reachable_dict.items():
        all_reachable_lst = []
        for n in neighbours:
            all_reachable_lst = all_reachable_lst + reachable_dict[n]
            all_reachable_lst = all_reachable_lst + [n]
        all_reachable[i] = all_reachable_lst
    return all_reachable

def exists_path2(matrix, origin, destination):
    reachable = reachable_dict(matrix)
    if not origin in reachable:
        return False
    else:
        return destination in reachable[origin]