class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # k %= len(nums)
        seen = set()
        seen.add(nums[0])
        L = 0
        for R in range(1,len(nums)):
            while R - L > k:
                seen.remove(nums[L])
                L += 1
            if nums[R] in seen:
                return True
            seen.add(nums[R])

        return False