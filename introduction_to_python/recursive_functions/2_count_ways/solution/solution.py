# Write your solution here
def stairs(n):
    if n <= 1:
        return n
    else:
        return stairs(n - 1) + stairs(n - 2)
def count_ways(steps):
    return stairs(steps + 1)
