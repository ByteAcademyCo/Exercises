# Code your solution here
def f(*args):
    return list(map(lambda x: x % 13 == 0))
result = f
print(result)