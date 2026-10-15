class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)

    def merge(self,nums1,nums2):
        combined = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j]) 
                j += 1
        while i< n1:
            combined.append(nums1[i])
            i += 1
        while j< n2:
            combined.append(nums2[j])
            j += 1
        return combined


        