class Solution:
    def sortColors(self, nums: list[int]) -> None:
        counted = [0,0,0]
        for i in nums:
            counted[i] += 1
        index = 0
        for i in range(3):
            for _ in range(counted[i]):
                nums[index] = i
                index += 1
        