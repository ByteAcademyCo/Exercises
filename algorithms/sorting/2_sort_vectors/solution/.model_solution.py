import math

def magnitude(vector):
    return math.sqrt((vector[0][0] - vector[1][0])**2 + (vector[0][1] - vector[1][1])**2)

def sort_vectors(vector_lst):
    for index in range(1, len(vector_lst)):
        currentvector = vector_lst[index]
        position = index
        while position>0 and magnitude(vector_lst[position-1])>magnitude(currentvector):
            vector_lst[position]=vector_lst[position-1]
            position = position-1
        vector_lst[position]=currentvector
    return vector_lst

vects = [((1, 3), (2, 6)), ((1, 5), (3, 4)), ((2, 6), (2, 9))]

print(sort_vectors(vects))