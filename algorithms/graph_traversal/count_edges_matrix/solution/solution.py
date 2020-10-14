def count_edges(matrix):
    edge_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            edge_count += matrix[i][j]
    return edge_count