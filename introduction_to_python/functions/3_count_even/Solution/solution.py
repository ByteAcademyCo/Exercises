def count_even(*args):
    return len(list(filter(lambda x: x % 2 == 0, args)))