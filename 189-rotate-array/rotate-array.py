class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        L = 0
        R = k - 1
        while L < R:
            nums[L],nums[R] = nums[R],nums[L]
            L += 1
            R -= 1
        L = k
        R = len(nums) - 1
        while L < R:
            nums[L],nums[R] = nums[R],nums[L]
            L += 1
            R -= 1