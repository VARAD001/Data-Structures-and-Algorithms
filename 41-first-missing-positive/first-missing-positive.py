class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        least = 1
        seen = set()
        for i in nums:
            if i == least:
                least += 1
                while least in seen:
                    least += 1
            seen.add(i)
        return least
        