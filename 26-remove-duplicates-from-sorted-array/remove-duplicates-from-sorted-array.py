class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        k = 1
        while fast < len(nums):
            if nums[fast] > nums[slow]:
                slow += 1
                nums[slow] = nums[fast]                
                k += 1
            # if nums[slow] == nums[fast]:
            #     slow = fast
            fast += 1
        return k
        