def paths_nth_stair(n):
    if n <= 2:
        return n
    else:
        memo = [-1 for i in range(n+1)]
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]