class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        length = 1
        mlength = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] +1:
                length += 1
            else:
                mlength = max(mlength,length)
                length = 1
        mlength = max(mlength,length)
        return mlength
