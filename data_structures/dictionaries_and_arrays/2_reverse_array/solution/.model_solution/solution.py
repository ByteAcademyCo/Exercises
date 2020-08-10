from array import array


def reverse(array_num):
    reverse_array = array("i")
    for i in range(len(array_num) - 1, -1, -1):
        reverse_array.append(array_num[i])
    return reverse_array
