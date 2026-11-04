class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indices = {}
        for i, a in enumerate(nums):
            if a in indices:
                for j in indices[a]:
                    if i - j <= k:
                        return True
                indices[a].append(i)
            else:
                indices[a] = [i]
        return False 