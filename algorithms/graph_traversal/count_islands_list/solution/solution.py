def count_islands(adjacency_list):
    dict_count_edges = dict.fromkeys(adjacency_list.keys(), 0)
    for adjkeyNode, edge_lst in adjacency_list.items():
        for keyNode in dict_count_edges.keys():
            if not adjkeyNode == keyNode:
                if keyNode in edge_lst:
                    dict_count_edges[keyNode] += 1
    numIslands = 0
    for edgeCount in dict_count_edges.values():
        if edgeCount == 0:
            numIslands += 1
    return numIslands