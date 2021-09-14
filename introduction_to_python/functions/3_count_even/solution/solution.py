def count_even(*args):
    for num in args:
        if num % 2 == 0:
            return num 

count_even(1, 2, 3, 4) == 2
