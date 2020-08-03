def count_even(*args):
<<<<<<< HEAD
    return list(map(lambda x: x % 2== 0))
=======
# Code your solution here
def f(*args):
    return list(map(lambda x: x % 2== 0))
result = f
print(result)
>>>>>>> 6cffc71... Completed Exercises
=======
    return len(list(filter(lambda x: x % 2 == 0, args)))
>>>>>>> 3f12b16... Updated and completed
