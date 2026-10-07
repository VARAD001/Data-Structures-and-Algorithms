class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        if nums.count(0)>1:
            return [0]*len(nums)
        total = nums[0]
        for i in nums[1:]:
            total *= i
        print(total)
        if total == 0:
            for i in nums:
                if total == 0 or i == 0:
                    total += i
                else:
                    total *= i
            for i in nums:
                if i == 0:
                    res.append(total)
                else:
                    res.append(0)
        else:
            for i in nums:
                res.append(int(total/i))
        return res