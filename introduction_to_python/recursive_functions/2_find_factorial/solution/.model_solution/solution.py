def factorial_recursive(n):
    return 1 if (n == 1 or n == 0) else n * factorial_recursive(n-1)

