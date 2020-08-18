def hops_away(adjacency_list, node, num_hops):
    if not node in adjacency_list.keys():
        return []
    elif num_hops == 0:
        return [node]
    else:
        number_hops_away = []
        for neighbour in adjacency_list[node]:
            number_hops_away.extend(hops_away(adjacency_list, neighbour, num_hops-1))
        number_hops_away_1 = []
        for n in number_hops_away:
            if not n in number_hops_away_1:
                number_hops_away_1.append(n)
        return number_hops_away_1