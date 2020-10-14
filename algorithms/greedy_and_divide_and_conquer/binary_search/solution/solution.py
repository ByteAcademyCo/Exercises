def binary_search_helper(lst, x, low, high): 
    if high >= low: 
        # Get index of middle element in lst
        mid = (high + low) // 2
        # If element is at mid idx
        if lst[mid] == x: 
            return mid 
        # If element is smaller than mid, then it will be in left subarray 
        elif lst[mid] > x: 
            return binary_search_helper(lst, x, low, mid - 1) 
        # Else the element can only be present in right subarray 
        else: 
            return binary_search_helper(lst, x, mid + 1, high) 
  
    else: 
        # Element is not present in the array 
        return -1

def binary_search(lst, x):
    return binary_search_helper(lst, x, 0, len(lst)-1)
