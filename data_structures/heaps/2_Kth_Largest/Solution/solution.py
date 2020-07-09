import heapq

class Solution(object):
    def find_Kth_Largest(self, nums, k):
        """
        :type nums: List[int]
        :type of k: int
        :return value type: int
        """
        h = []
        for e in nums:
            heapq.heappush(h, (-e, e))
        for i in range(k):
            w, e = heapq.heappop(h)
            if i == k - 1:
                return e

arr_nums = [12, 14, 9, 50, 61, 41]
s = Solution()
result = s.find_Kth_Largest(arr_nums, 3)
print(result)