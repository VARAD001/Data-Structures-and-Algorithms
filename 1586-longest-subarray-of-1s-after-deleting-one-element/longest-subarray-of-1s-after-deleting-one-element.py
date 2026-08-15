class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        answer = 0
        L = 0
        for R in range(len(nums)):
            if nums[R] == 0:
                zeros += 1
            while zeros > 1:
                if nums[L] == 0:
                    zeros -=1
                L += 1
            length = R - L
            answer = max(length,answer)
        return answer
        