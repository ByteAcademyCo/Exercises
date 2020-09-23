def fibonacci_bad(n):
    def helper(n, counter=1, previous=1, second_previous=1):
        if counter == n:
            return second_previous
        else:
            return helper(n, counter + 1, previous + second_previous, previous)

    return helper(n)


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(2))
