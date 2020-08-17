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