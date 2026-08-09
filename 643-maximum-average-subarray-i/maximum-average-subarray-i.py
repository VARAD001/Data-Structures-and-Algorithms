class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L = 0
        max_avg = float('-inf')
        max_window = 0
        for R in range(len(nums)):
            max_window += nums[R]
            if R-L+1 == k:
                max_avg = max(float(max_avg),float((max_window)/k))
                max_window -= nums[L]
                L += 1
        return max_avg