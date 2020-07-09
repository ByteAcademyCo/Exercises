import heapq as hq
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
# Find three smallest values
smallest_nums = hq.nsmallest(3, nums_list)
print(smallest_nums)
