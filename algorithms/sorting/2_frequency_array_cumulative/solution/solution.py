def frequency_array(lst):
    maximum = -1
    for i in lst:
        if i > maximum:
            maximum = i
    frequency_lst = [0 for i in range(maximum + 1)]
    for i in range(len(lst)):
        frequency_lst[lst[i]] += 1
    return frequency_lst

def frequency_array_cumulative(lst):
    frequency_lst = frequency_array(lst)
    frequency_length = len(frequency_lst)
    frequency_list = [0 for i in range(frequency_length)]
    for i in range(frequency_length):
        if i == 0:
            frequency_list[i] = frequency_lst[i]
        else:
            frequency_list[i] = frequency_lst[i] + frequency_list[i-1]  
    return frequency_list