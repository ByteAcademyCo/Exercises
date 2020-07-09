import heapq as hq
nums_list = [18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1]
hq.heapify(nums_list)
s_result = [hq.heappop(nums_list) for i in range(len(nums_list))]

print(s_result)