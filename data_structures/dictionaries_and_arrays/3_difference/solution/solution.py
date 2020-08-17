# Write your solution here
def difference(array_num):
    numbers = sorted(array_num)
    result = numbers[-1] - numbers[0]
    return result