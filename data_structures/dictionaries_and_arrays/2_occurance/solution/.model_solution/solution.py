from array import *
def occurance(array_num,element):
    count = 0
    for i in array_num:
        if i == element:
            count +=1
    return count 