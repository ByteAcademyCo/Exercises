# Code your solution here
l = [10, 20, 30, 40, 50, 60]
# l = [1, 2, 3, 4, 5]
# used the list provided in test_solution.py for the test to work

def a_list(l):
    summ = 0
    for i in l:
        summ += i
        return summ
result = a_list(l)
print(result)