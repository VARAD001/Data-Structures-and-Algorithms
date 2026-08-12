class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        count = 0
        length =0
        L = 0
        for R in range(len(nums)):
            window += nums[R]
            length += 1
            while window>=target:
                if not count:
                    count = length
                else:
                    count = min(count,length)
                window-=nums[L]
                length -= 1
                L += 1
        return count
        