def binomial_coefficient(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if n == 1:
        return 0
    else:
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

