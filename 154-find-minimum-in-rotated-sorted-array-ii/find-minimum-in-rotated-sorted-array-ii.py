class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # The minimum element must be in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # The minimum element is in the left half or at mid
                right = mid
            else:
                # When nums[mid] == nums[right], we can't decide the direction,
                # so we safely shrink the search space by decrementing right.
                right -= 1

        return nums[left]