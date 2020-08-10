from array import array


def difference(array_num):
    greatest = 0
    smallest = 0
    for i in range(len(array_num)):
        if greatest < array_num[i]:
            greatest = array_num[i]
    smallest = greatest
    for i in range(len(array_num)):
        if smallest > array_num[i]:
            smallest = array_num[i]
    result = greatest - smallest
    return result
