class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq = {}
        for i in arr1:
            freq[i] = freq.get(i,0) + 1
        new = []
        for i in arr2:
            new.extend([i]*(freq[i]))
            del freq[i]
        for a in sorted(freq.keys()):
            new.extend([a]*freq[a])
        return new