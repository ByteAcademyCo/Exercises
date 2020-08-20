import math

def magnitude(vector):
    return math.sqrt((vector[0][0]-vector[1][0])**2 + (vector[0][1]-vector[1][1])**2)

def sort_vectors(vector_lst):
    for index in range(1, len(vector_lst)):
        current_vector = vector_lst[index]
        position = index
        while position > 0 and magnitude(vector_lst[position-1]) > magnitude(current_vector):
            vector_lst[position] = vector_lst[position-1]
            position -= 1
        vector_lst[position] = current_vector
    return vector_lst