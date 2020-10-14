def frequency_array(lst):
    # max_elem is variable we will use to store the largest
    # element in our list
    max_elem = -1
    # itterate through our elements to find the 
    # largest element in lst.
    for i in lst:
        if i > max_elem:
            max_elem = i
    # create a list of all 0s of len(max_elem)
    # freq_lst will keep track of each time we see an element
    # to count the number of times it appears in lst.
    freq_lst = [0 for i in range(max_elem+1)]
    # itterate through elements in lst, for each element we add
    # 1 to the value in freq list at the index of that value.
    for elem in lst:
        freq_lst[elem] += 1
    # return the freq_lst
    return freq_lst