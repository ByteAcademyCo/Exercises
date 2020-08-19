def binary_search_helper(lst, x, low, high): 
    if high >= low: 
        mid = (high + low) // 2
        if lst[mid] == x: 
            return mid 
        elif lst[mid] > x: 
            return binary_search_helper(lst, x, low, mid - 1) 
        else: 
            return binary_search_helper(lst, x, mid + 1, high) 
    else: 
        return -1

def binary_search(lst, x):
    return binary_search_helper(lst, x, 0, len(lst)-1)
