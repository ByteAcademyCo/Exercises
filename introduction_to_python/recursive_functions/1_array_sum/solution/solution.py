# Write your solution here
def sum_array(num_list):
    if num_list == []:
        return 0
    else:
        return num_list.pop() + sum_array(num_list)