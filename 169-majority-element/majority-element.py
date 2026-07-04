class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = {}
        for i in range(len(nums)):
            if nums[i] not in data.keys():
                data[nums[i]] = 1
            else:
                data[nums[i]] +=1
        for j in range(len(nums)):
            if data[nums[j]] >  (len(nums)/2):
                return nums[j]