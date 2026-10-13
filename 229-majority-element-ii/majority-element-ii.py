class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)/3
        freq = {}
        res = set()
        for i in nums:
            freq[i] = freq.get(i,0) + 1
            if freq[i]> n and i not in res:
                res.add(i)
        return list(res)
