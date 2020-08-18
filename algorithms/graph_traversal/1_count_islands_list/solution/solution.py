def count_islands(adjacency_list):
    dictionary_count_edges = dict.fromkeys(adjacency_list.keys(), 0)
    for adj_keyNode, edge_list in adjacency_list.items():
        for keyNode in dictionary_count_edges.keys():
            if not adj_keyNode == keyNode:
                if keyNode in edge_list:
                    dictionary_count_edges[keyNode] += 1
    number_of_Islands = 0
    for edgeCount in dictionary_count_edges.values():
        if edgeCount == 0:
            number_of_Islands += 1
    return number_of_Islands

#adjacency_list = { 0: [1], 1: [0, 1, 2], 2: []}

# dictionary_count_edges -> assigns every key:value pair to 0

#dictionary_count_edges = {0:0, 1:0, 2: 0}
#for every key and list in adjacency_list
#0 : [1]
#1 : [0, 1, 2]
#2 : []

#dictionary_count_edges = {0:2, 1:1, 2:1}
# for every key in dictionary_count_edges
# 0 -> in 0 and 1 so increment by 2
# 1 -> in 0 so increment by 1
# 2 -> in 1 so increment by 1