def frequency_array(lst):
    maximum = -1
    for i in lst:
        if i > maximum:
            maximum = i
    frequency_lst = [0 for i in range(maximum + 1)]
    for i in range(len(lst)):
        frequency_lst[lst[i]] += 1
    return frequency_lst
