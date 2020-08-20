def sort_tuples(tup):   
    tup.sort(key = lambda t: t[1])  
    tup.reverse()
    return tup

def steal_jewels(x, jewels):
    # max_val will keep track of the max_val we can add to our bag.
    max_val = 0
    # we sort the list of jewel tuples in decresing order by value.
    # so the highet value jewel will be at the first of the list.
    sorted_value_jewels = sort_tuples(jewels)
    # we loop through the list of jewel tuples
    for jewel in sorted_value_jewels:
        jewel_weight = jewel[0]
        jewel_value = jewel[1]
        # if our bag weight capacity is 0 we return the maximum value 
        # we've added to our bag max_val.
        if x == 0:
            return max_val
        # if the weight of the current jewel is <= x we add it to our bag
        # and update the capacity of our bag, and update the max_value we 
        # have so far.
        elif jewel_weight <= x:
            max_val += jewel_value
            x = x-jewel_weight
        else:
            # if the jewel weight is larger than the capacity of our bag,
            # we calculate the value of a 1kg portion of the jewel
            unit_val = jewel_value/jewel_weight
            # we add an xkg portion of the jewel to our bag 
            max_val += x * unit_val
            # our bag is now full and we return max_val
            return max_val
    # after we itterate through all the jewels, we've added everything we can
    # so we return max_val
    return max_val

jewels = [(1, 4), (2, 8), (3, 15), (9, 50)]
print(steal_jewels(10, jewels))