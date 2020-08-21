def paths_nth_stair(n):
    if n <= 2:
        return n
    else:
        paths = [-1 for x in range(n+1)]
        paths[1] = 1
        paths[2] = 2
        for x in range(3, n+1):
            paths[x] = paths[x-1] + paths[x-2]
        return paths[n]