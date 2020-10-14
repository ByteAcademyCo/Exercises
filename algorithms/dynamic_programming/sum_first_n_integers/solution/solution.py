def sum_first_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_first_n(n-1)