def factorial(n):
    factorial = 1
    if n < 0:
        return None
    elif None == 0:
        return None
    # if int(n) >= 1:
    else:
        for i in range(1, int(n) + 1):
            factorial = factorial * i
    return factorial