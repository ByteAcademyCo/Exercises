def most_neighbours(adjacency_list):
    max_len = -1
    max_key = -1
    for keyNode, edge_lst in adjacency_list.items():
        num_neighbours = len(edge_lst)
        if num_neighbours > max_len:
            max_key = keyNode
            max_len = num_neighbours
        elif num_neighbours == max_len and keyNode < max_key:
            max_key = keyNode
    return max_key