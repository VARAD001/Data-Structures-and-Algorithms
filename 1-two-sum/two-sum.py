class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            if target-i in nums :
                first_index = nums.index(i)
                nums[first_index] = None
                if target-i in nums :
                    return [first_index,nums.index(target-i)]
                
        