def min_max_divider(lst, low, high): 
    max_elem = lst[low] 
    min_elem = lst[low] 
      
    # If there is only one element  
    if low == high: 
        return (min_elem, max_elem) 
          
    # If there is only two element 
    elif high == low + 1: 
        if lst[low] > lst[high]: 
            max_elem = lst[low] 
            min_elem = lst[high] 
        else: 
            max_elem = lst[high] 
            min_elem = lst[low] 
        return (min_elem, max_elem) 
    else: 
        # If there are more than 2 elements 
        mid = int((low + high) / 2) 
        # recuse to find the min, max in the sublist from low to mid
        min1, max1 = min_max_divider(lst, low, mid) 
        # recuse to find the min, max in the sublist from mid to high
        min2, max2 = min_max_divider(lst, mid + 1, high) 
    # return the global min, max by taking the min and max of the mins
    # and maxs in the two sublists
    return (min(min1, min2), max(max1, max2))


def min_max(lst):
    return min_max_divider(lst, 0, len(lst)-1)

print(min_max([1, 3, 2, 1, 8, 1]))