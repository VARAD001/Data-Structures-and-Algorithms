class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)/3
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        res = []
        for i in freq:
            if freq[i] > n:
                res.append(i)
        return res
        