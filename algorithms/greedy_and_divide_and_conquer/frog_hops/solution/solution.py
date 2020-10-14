def min_hops_helper(max_units, n, river, num_hops):
    # Frog starts at position 0
    position = 0
    # Frog can hop up to max_units. We want to hop as far as we can
    # So we itterate through from max_units backwards to 0 to find the
    # largest jump we can make.
    for i in range(max_units, 0, -1):
        # Check if our current position + i the number of hops we want to make
        # is less than or equal to our final destination poition n.
        # and check if there is a lily pad a position + i.
        # if there is a lily pad at position + i, we can hop there!
        if position + i <= n and river[position + i] == 1:
            # After we hop i units we update num hops by 1
            # and we are now at position + i
            num_hops += 1
            position = position + i
            # we then recurse updating our destitination to n-i, 
            # updating river to now start at our current position.
            return min_hops_helper(max_units, n-i, river[position:], num_hops)
    # If we got to position == n we made it! so we return the total num_hops we made.
    if position == n:
        return num_hops
    # Otherwise we couldn't make it to position n and we return -1.
    else:
        return -1

def min_hops(max_units, n, river):
    return min_hops_helper(max_units, n, river, 0)

print(min_hops(3, 7, [1, 0, 0, 1, 1, 0, 0, 1]))