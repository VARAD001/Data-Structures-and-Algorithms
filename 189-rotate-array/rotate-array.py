class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k >= len(nums):
            k %= len(nums)
        print(k)

        nums[:] = nums[-k:] + nums[:-k]