def shortest_path_to_1(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    memo = [-1 for i in range(n+1)]
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1
    for i in range(4, n+1):
        if memo[i] == -1:
            if i%3 == 0 and i%2 == 0:
                memo[i] = 1 + min(memo[i-1], memo[i//3], memo[i//2])
            elif i%3 == 0:
                memo[i] = 1 + min(memo[i-1], memo[i//3])
            elif i%2 == 0:
                memo[i] = 1 + min(memo[i-1], memo[i//2])
            else:
                memo[i] = 1 + memo[i-1]
    return memo[n]