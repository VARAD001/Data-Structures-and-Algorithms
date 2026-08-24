class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        res = [0]*n
        L = 0
        R = n - 1
        for i in range(n-1,-1,-1):
            left = nums[L] **2
            right = nums[R] **2
            if left > right:
                res[i] = left
                L += 1
            else:
                res[i] = right
                R -= 1
        return res
        