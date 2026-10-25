class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new = [None]*len(nums)
        index = 0
        seen = set()
        for i in nums:
            if i not in seen:
                new[index] = i
                seen.add(i)
                index += 1
        nums[:] = new
        return len(seen)
         
        