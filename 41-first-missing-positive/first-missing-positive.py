class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Replace invalid numbers
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Negative marking
        for i in range(n):
            x = abs(nums[i])

            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])

        # Find the first unmarked number
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
        