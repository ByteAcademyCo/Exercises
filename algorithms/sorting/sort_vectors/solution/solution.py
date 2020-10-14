import math

def magnitude(vector):
    # calculate magnitude of a vector
    return math.sqrt((vector[0][0] - vector[1][0])**2 + (vector[0][1] - vector[1][1])**2)

def sort_vectors(vector_lst):
    return sorted(vector_lst, key=lambda vector: magnitude(vector))

vects = [((1, 3), (2, 6)), ((1, 5), (3, 4)), ((2, 6), (2, 9))]