def frequency_array(lst):
    max_elem = -1
    for i in lst:
        if i > max_elem:
            max_elem = i
    freq_lst = [0 for i in range(max_elem+1)]

    for i in range(len(lst)):
        freq_lst[lst[i]] += 1
    return freq_lst

def frequency_array_cumulative(lst):
    # create frequency array as question 1.
    freq_lst = frequency_array(lst)
    freq_len = len(freq_lst)
    # initialise freq_cum_list with all 0 values.
    freq_cum_lst = [0 for i in range(freq_len)]
    # itterate through indices in the freq_list 
    for i in range(freq_len):
        # at index 0, the freq_cum_list will be the same as the freq_lst at 0
        if i == 0:
            freq_cum_lst[i] = freq_lst[i]
        # at every index > 0 we add the previous frequency count with the new freq_lst[i]
        else:
            freq_cum_lst[i] = freq_lst[i] + freq_cum_lst[i-1]
    return freq_cum_lst

print(frequency_array_cumulative([1, 1, 4, 3, 8, 5, 9, 8, 8, 4, 6]))