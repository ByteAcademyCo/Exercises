from array import array
arr = array('i', [1, 2, 3, 4, 5])
ins_pos = int(input("enter the position where value to be inserted"))
ins_val = int(input("enter the value to be insterted"))
arr.insert(ins_pos,ins_val)
print(arr)
