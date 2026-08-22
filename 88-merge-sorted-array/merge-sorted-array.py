class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        left = nums1[:m]
        right = nums2
        combined = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                combined.append(left[i])
                i += 1
            else:
                combined.append(right[j])
                j += 1
        while i < len(left):
            combined.append(left[i])
            i += 1
        while j < len(right):
            combined.append(right[j])
            j += 1
        for i in range(len(nums1)):
            nums1[i] = combined[i]