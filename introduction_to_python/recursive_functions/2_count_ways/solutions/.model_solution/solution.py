def fib(n): 
    return n if n <= 1 else fib(n-1) + fib(n-2)

def count_ways(s): 
    return fib(s + 1)

