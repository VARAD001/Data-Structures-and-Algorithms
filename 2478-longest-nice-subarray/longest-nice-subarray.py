class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        bitwise_and = 0
        res = 0
        L = 0
        for R in range(len(nums)):
            while L < R and bitwise_and & nums[R] != 0:
                bitwise_and ^= nums[L]
                L += 1
            bitwise_and |= nums[R]
            res = max(res, R - L + 1)

        return res
        