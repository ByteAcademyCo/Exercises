def min_hops_helper(max_units, n, river, num_hops):
    position = 0
    for i in range(max_units, 0, -1):
        if position + i <= n and river[position + i] == 1:
            num_hops += 1
            position = position + i
            return min_hops_helper(max_units, n-i, river[position:], num_hops)
    if position == n:
        return num_hops
    else:
        return -1

def min_hops(max_units, n, river):
    return min_hops_helper(max_units, n, river, 0)

print(min_hops(3, 7, [1, 0, 0, 1, 1, 0, 0, 1]))