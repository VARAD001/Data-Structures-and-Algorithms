class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
                if nums[i] == val:
                    nums.pop(i)
                    # nums.append("_")
                else:
                    k += 1
                    i+= 1
        return k
        