def frequency_array(lst):
    max_elem = -1
    for i in lst:
        if i > max_elem:
            max_elem = i
    freq_lst = [0 for i in range(max_elem+1)]

    for i in range(len(lst)):
        freq_lst[lst[i]] += 1
    return freq_lst
