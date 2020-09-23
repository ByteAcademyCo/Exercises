def shortest_path_to_1(n):
    # if n is 1 we need 0 steps to get to 1
    if n == 1:
        return 0
    # if n is 2 or 3, we only need one step to get to 1
    if n == 2 or n == 3:
        return 1
    # create a memo list. memo[i] will store the number of steps 
    # to get to the ith stair. We initialise the values to -1.
    memo = [-1 for i in range(n+1)]
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1
    for i in range(4, n+1):
        # if i is divisible by 2 and 3 the shortest path will be 
        # 1 + the minimum path for i-1, i/2 or i/3. We already
        # have those values calculated and stored in our memo list.
        if i%3 == 0 and i%2 == 0:
            memo[i] = 1 + min(memo[i-1], memo[i//3], memo[i//2])
        # if i is divisible by 3 the shortest path will be 
        # 1 + the minimum path for i-1, or i/3.
        elif i%3 == 0:
            memo[i] = 1 + min(memo[i-1], memo[i//3])
        # if i is divisible by 2 the shortest path will be 
        # 1 + the minimum path for i-1, or i/2.
        elif i%2 == 0:
            memo[i] = 1 + min(memo[i-1], memo[i//2])
        else:
            memo[i] = 1 + memo[i-1]
    return memo[n]
