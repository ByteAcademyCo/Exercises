# Code your solution here
def div_by_3(*args):
    return list(filter(lambda x: x % 3 == 0, args))