def square_keys(num):
    my_dict = dict()
    for i in range(1, num + 1):
        my_dict[i] = i ** 2
    return my_dict

def square_keys_alternative(num):
    return {i: i**2 for i in range(1,num+1)}
