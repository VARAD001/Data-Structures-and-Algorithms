class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        new = [0]*len(nums)
        k %= len(nums)
        for i in range(len(nums)):
            new[(i + k)%len(nums)] = nums[i]
        nums[:] = new