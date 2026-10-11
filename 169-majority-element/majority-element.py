class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)/2
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        for i in freq:
            if freq[i] > n:
                return i