def paths_nth_stair(n):
    # if n is 0, 1, or 2, the number of ways to climb up is just n.
    if n <= 2:
        return n
    else:
        # we create a memo list to keep track of the number of ways to climb to
        # the ith stair. We initialise the values to -1.
        memo = [-1 for i in range(n+1)]
        # we know the ways to climb to the 1st stair is 1 so memo[1] = 1
        memo[1] = 1
        # we know the ways to climb to the 2nd stair is 2 so memo[2] = 2
        memo[2] = 2
        # we itterate through the rest of the indices, and notice the
        # recurrence relation, the number of ways to get to the ith stair
        # will be to start by climbing up 1 stair and then climbing up i-1 stairs
        # or climbing up 2 stairs and then climbing up i-2 stairs
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]