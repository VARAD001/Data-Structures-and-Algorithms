class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        count = 0
        L = 0
        for R in range(len(nums)):
            window += nums[R]
            while window>=target:
                length = R - L + 1
                if not count:
                    count = length
                else:
                    count = min(count,length)
                window-=nums[L]
                L += 1
        return count
