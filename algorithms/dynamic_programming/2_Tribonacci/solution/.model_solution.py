def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # create a memo list to store the ith tribonacci number at memo[i]
    memo = [-1 for i in range(n+1)]
    memo[0] = 0
    memo[1] = 0
    memo[2] = 1
    for i in range(3, n+1):
        memo[i] = memo[i-3] + memo[i-2] + memo[i-1]
    return memo[i]

print(tribonacci(2))