def shortest_path_to_1(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    shortest = [-1 for x in range(n+1)]
    shortest[1] = 0
    shortest[2] = 1
    shortest[3] = 1
    for x in range(4, n+1):
        if shortest[x] == -1:
            if x % 3 == 0 and x % 2 == 0:
                shortest[x] = 1 + min(shortest[x-1], shortest[x//3], shortest[x//2])
            elif x % 3 == 0:
                shortest[x] = 1 + min(shortest[x-1], shortest[x//3])
            elif x % 2 == 0:
                shortest[x] = 1 + min(shortest[x-1], shortest[x//2])
            else:
                shortest[x] = 1 + shortest[x-1]
    return shortest[n]


