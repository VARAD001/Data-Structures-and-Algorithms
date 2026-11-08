class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        mimi = 100000000
        L = 0
        current = 0
        for R in range(len(nums)):
            current += nums[R]
            while current >= target:
                mimi = min(mimi,R-L+1)
                current -= nums[L]
                L += 1
        if mimi < 100000000:
            return mimi
        else:
            return 0

        