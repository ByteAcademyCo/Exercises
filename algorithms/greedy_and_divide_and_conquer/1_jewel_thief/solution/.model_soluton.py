def sort_tuples(tup):   
    tup.sort(key = lambda t: t[1])  
    tup.reverse()
    return tup

def steal_jewels(x, jewels):
    max_val = 0
    sorted_value_jewels = sort_tuples(jewels)
    for jewel in sorted_value_jewels:
        jewel_weight = jewel[0]
        jewel_value = jewel[1]
        if x == 0:
            return max_val
        elif jewel_weight <= x:
            max_val += jewel_value
            x = x-jewel_weight
        else:
            # value of 1kg portion of the jewel
            unit_val = jewel_value/jewel_weight
            max_val += x * unit_val
            return max_val
    return max_val

jewels = [(1, 4), (2, 8), (3, 15), (9, 50)]
print(steal_jewels(10, jewels))