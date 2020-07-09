import heapq as hq
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
# Find three largest values
largest_nums = hq.nlargest(3, nums_list)
print(largest_nums)
