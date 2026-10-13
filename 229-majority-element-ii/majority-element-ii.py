class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count1 = 0
        count2 = 0
        candidate1, candidate2 = None, None
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        target = len(nums)/3
        res = []
        if nums.count(candidate1) > target:
            res.append(candidate1)
        if nums.count(candidate2) > target and candidate1!=candidate2:
            res.append(candidate2)       
        return res     
