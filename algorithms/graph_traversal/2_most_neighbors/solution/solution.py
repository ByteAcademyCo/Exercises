def most_neighbours(adjacency_list):
    maximum_len = -1
    maximum_key = -1
    for keyNode, edge_list in adjacency_list.items():
        number_of_neighbours = len(edge_list)
        if number_of_neighbours > maximum_len:
            maximum_key = keyNode
            maximum_len = number_of_neighbours
        elif number_of_neighbours == maximum_len and keyNode < maximum_key:
            maximum_key = keyNode
    return maximum_key