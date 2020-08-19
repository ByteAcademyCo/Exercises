def helper_min_max(lst, low, high): 
    maximum = lst[high] 
    minimum = lst[low] 
    if low == high: 
        return (minimum, maximum) 
    elif low + 1 == high: 
        if lst[low] > lst[high]: 
            maximum = lst[low] 
            minimum = lst[high] 
        else: 
            maximum = lst[high] 
            minimum = lst[low] 
        return (minimum, maximum) 
    else: 
        mid = int((low + high) / 2) 
        min1, max1 = helper_min_max(lst, low, mid) 
        min2, max2 = helper_min_max(lst, mid + 1, high) 
    return (min(min1, min2), max(max1, max2))
def min_max(lst):
    return helper_min_max(lst, 0, len(lst)-1)