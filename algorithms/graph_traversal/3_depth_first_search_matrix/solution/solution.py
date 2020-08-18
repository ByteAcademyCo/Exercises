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

# matrix = [ [0, 1, 0], [0, 0, 1], [0, 1, 0] ]

# exists_path(matrix, 0, 2) => True

# exists_path_visited(matrix, 0, 2, [])

# visited = [0]
# for j = 0, 1, 2
#                     matrix, j, destination, visitedlist
# exists_path_visited(matrix, 1, 2, [0])

#matrix[1][2] == 1, so we would return True