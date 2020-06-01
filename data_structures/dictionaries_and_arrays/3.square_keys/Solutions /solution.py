def square_keys(num):
    my_dict = dict()
    for i in range(1,num+1):
        my_dict[i]=i**2
    return my_dict
num=int(input("Input a number "))
result = square_keys(num)
print(result)