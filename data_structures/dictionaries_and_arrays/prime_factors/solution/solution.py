from math import sqrt

def is_prime(x):
    # itterate through numbers 2...sqrt(n)
    for i in range(2, int(sqrt(x)+1)):
        # if i is a factor of x, x is not prime
        if x%i == 0:
            return False
    # if we found no factors x is prime
    return True

def prime_factors(n):
    # list to keep track of prime factors
    factors = []
    # loop through numbers 1...n
    for i in range(1, n+1):
        # if i is a factor of n and i is prime
        if n%i == 0 and is_prime(i):
            # append i to our prime factors list
            factors.append(i)
    return factors
