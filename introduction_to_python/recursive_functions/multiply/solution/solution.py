def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)
