from array import array 
array_num = array('i', [5, 8, 12, 15, 10, 7])
greatest=0
smallest=0
for i in range(len(array_num)):
    if greatest<array_num[i]:
        greatest=array_num[i]
smallest=greatest
for i in range(len(array_num)):
    if smallest>array_num[i]:
        smallest=array_num[i]
result=greatest-smallest
print(result)