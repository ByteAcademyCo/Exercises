def sib_compare(sib_tup1, sib_tup2):
    # if age of sib1 < age of sib2 
    if sib_tup1[1] < sib_tup2[1]:
        return "less"
    # if ages are equal, compare names of sibs
    elif sib_tup1[1] == sib_tup2[1] and sib_tup1[0] < sib_tup2[0]:
        return "less"
    else:
        return "greater"

def merge_sort_tuples(tuple_lst):
    if len(tuple_lst) > 1: 
        mid = len(tuple_lst)//2 # Finding the mid of the array 
        L = tuple_lst[:mid] # Dividing the array elements  
        R = tuple_lst[mid:] # into 2 halves 
  
        merge_sort_tuples(L) # Sorting the first half 
        merge_sort_tuples(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if sib_compare(L[i], R[j]) == "less": 
                tuple_lst[k] = L[i] 
                i+= 1
            else: 
                tuple_lst[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            tuple_lst[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            tuple_lst[k] = R[j] 
            j+= 1
            k+= 1
    return tuple_lst

def sort_siblings(sib_dict):
    tuple_lst = [(name, age) for name, age in sib_dict.items()]
    return merge_sort_tuples(tuple_lst)
    
sib_dict1 = {"Anton": 10,
            "Cosette": 3,
            "Nancy": 15,
            "Lucas": 15}

print(sort_siblings(sib_dict1))