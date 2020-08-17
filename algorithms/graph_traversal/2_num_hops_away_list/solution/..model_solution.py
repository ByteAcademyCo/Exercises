def hops_away(adjacency_list, node, num_hops):
    if not node in adjacency_list.keys():
        return []
    elif num_hops == 0:
        return [node]
    else:
        hops_away_neighbours = []
        for neighbour in adjacency_list[node]:
            hops_away_neighbours.extend(hops_away(adjacency_list, neighbour, num_hops-1))
        hops_away_neighbours_unique = []
        for n in hops_away_neighbours:
            if not n in hops_away_neighbours_unique:
                hops_away_neighbours_unique.append(n)
        return hops_away_neighbours_unique
