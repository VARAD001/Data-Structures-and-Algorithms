class Solution:
    def pivot(self,mylist,pivot_index,end):
        swap_index = pivot_index
        for i in range(pivot_index+1,end+1):
            if mylist[i]<mylist[pivot_index]:
                swap_index += 1
                mylist[swap_index],mylist[i] = mylist[i],mylist[swap_index]
        mylist[pivot_index],mylist[swap_index] = mylist[swap_index],mylist[pivot_index]
        return swap_index
    def quick_sort(self,mylist,left,right):
        if left < right:
            pivot_index = self.pivot(mylist,left,right)
            self.quick_sort(mylist,left,pivot_index-1)
            self.quick_sort(mylist,pivot_index+1,right)
        return mylist

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.quick_sort(nums,0,len(nums)-1)
        
