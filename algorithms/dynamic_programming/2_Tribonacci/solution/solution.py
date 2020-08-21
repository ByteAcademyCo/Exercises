# def tribonacci(n):
#     if n == 0 or n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return tribonacci(n-1) + tribonacci(n-2) +tribonacci(n-3)
def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    trib = [-1 for x in range(n+1)]
    trib[0] = 0
    trib[1] = 0
    trib[2] = 1
    for x in range(3, n+1):
        # trib[x] = trib[x-1] + trib[x-2] + trib[x-3]
        trib[x] = trib[x-3] + trib[x-2] + trib[x-1]    #to make the bottom-up tabulation make more sense
    return trib[x]
