def hofstaderA(n):
    if n == 0:
        return 1
    else:
        return n - hofstaderB(hofstaderA(n-1))


def hofstaderB(n):
    if n == 0:
        return 0
    else:
        return n - hofstaderA(hofstaderB(n-1))
