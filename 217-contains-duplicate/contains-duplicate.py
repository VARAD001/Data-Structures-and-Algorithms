class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if len(nums) <=1:
            return False
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False