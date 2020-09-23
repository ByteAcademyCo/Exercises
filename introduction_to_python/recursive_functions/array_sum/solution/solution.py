def sum_array(num_list):
    return 0 if num_list == [] else num_list[0] + sum_array(num_list[1:])
