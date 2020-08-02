<<<<<<< HEAD
<<<<<<< HEAD
# L = [152, 463, 1112, 1337, -10]
# LIST_MAX = sorted(L)[-1]

# print(LIST_MAX(L))

L = [152, 463, 1112, 1337, -10]
def LIST_MAX1(L):
    current_max = L[0]
    if L[1] > current_max:
        current_max = L[1]
    if L[2] > current_max:
        current_max = L[2]
    if L[3] > current_max:
        current_max = L[3]
    if L[4] > current_max:
        current_max = L[4]
    return current_max
LIST_MAX = LIST_MAX1(L)
=======
L = [152, 463, 1112, 1337, -10]
# def LIST_MAX(L):
#     if L == []:
#         LIST_MAX1 = None
#     else:
#         LIST_MAX1 = sorted(L)[-1]
#     return LIST_MAX1

# print(LIST_MAX(L))
LIST_MAX = sorted(L)[-1]
# print(LIST_MAX)
>>>>>>> d536594... Pushing exercises
=======
# L = [152, 463, 1112, 1337, -10]
# LIST_MAX = sorted(L)[-1]

# print(LIST_MAX(L))

L = [152, 463, 1112, 1337, -10]
def LIST_MAX1(L):
    current_max = L[0]
    if L[1] > current_max:
        current_max = L[1]
    if L[2] > current_max:
        current_max = L[2]
    if L[3] > current_max:
        current_max = L[3]
    if L[4] > current_max:
        current_max = L[4]
    return current_max
<<<<<<< HEAD
LIST_MAX = LIST_MAX1(L)

>>>>>>> f07cce6... Completed
=======
LIST_MAX = LIST_MAX1(L)
>>>>>>> 6cffc71... Completed Exercises
