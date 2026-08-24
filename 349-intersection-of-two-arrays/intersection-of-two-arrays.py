class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen  = set()
        ans = []
        for i in nums1:
            seen.add(i)
        for j in nums2:
            if j in seen:
                ans.append(j)
                seen.remove(j)
        return ans