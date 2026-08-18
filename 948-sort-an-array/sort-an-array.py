class Solution:
    def merge(self,list1,list2):
        combined = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                combined.append(list1[i])
                i+=1
            else:
                combined.append(list2[j])
                j += 1
        while i < len(list1):
            combined.append(list1[i])
            i += 1
        while j < len(list2):
            combined.append(list2[j])
            j += 1
        return combined


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        middle_index = len(nums)//2
        left = self.sortArray(nums[0:middle_index])
        right = self.sortArray(nums[middle_index:])
        return self.merge(left,right)

        
        