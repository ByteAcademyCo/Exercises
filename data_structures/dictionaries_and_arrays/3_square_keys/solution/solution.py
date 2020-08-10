# Write your solution here
def square_keys(num):
    dict = {}
    for x in range(1, num+1):
        dict[x] = x**2
    return dict