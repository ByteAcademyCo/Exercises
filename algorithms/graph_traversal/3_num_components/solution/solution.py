def reachable_dict(matrix):
    reachable_dict = {}
    for i in range(len(matrix)):
        reachable_lst = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                reachable_lst.append(j)
        reachable_dict[i] = reachable_lst
#getting every key that's directly reachable and putting it into a list
    all_reachable = {}
    for i, neighbours in reachable_dict.items():
        all_reachable_lst = []
        for n in neighbours:
            all_reachable_lst = all_reachable_lst + reachable_dict[n]
            all_reachable_lst = all_reachable_lst + [n]
        all_reachable[i] = all_reachable_lst
    return all_reachable
#getting every key that's neighbors of the directly reachables and putting it into a list

def num_components(adjacency_matrix):
    reachableDict = reachable_dict(adjacency_matrix)
    num_components = 0
    visited = [False for i in range(len(adjacency_matrix))]
    for i in range(len(adjacency_matrix)):
        if visited[i] == False:
            num_components += 1
            for j in reachableDict[i]:
                visited[j] = True
    return num_components

# visited [False, False, False, False]
# visited []