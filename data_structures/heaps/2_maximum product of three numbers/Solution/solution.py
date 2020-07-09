def maximumProduct(nums):
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
arr_nums = [12, 74, 9, 50, 61, 41]
result = maximumProduct(arr_nums)
print(result)
