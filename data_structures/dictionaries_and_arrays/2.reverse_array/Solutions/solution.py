from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
reverse_array = array('i')
for i in range(len(array_num)-1,-1,-1):
    reverse_array.append(array_num[i])
print(reverse_array)
