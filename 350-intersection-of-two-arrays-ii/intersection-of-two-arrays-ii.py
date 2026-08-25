class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in nums2:
            if i in nums1:
                nums1.remove(i) 
                ans.append(i)
        return ans