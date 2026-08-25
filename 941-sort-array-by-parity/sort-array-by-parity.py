class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L = 0
        R = len(nums) -1 
        while L < R:
            while L<R and nums[L] % 2 == 0:
                L += 1
            while L<R and nums[R] % 2 != 0:
                R-=1
            nums[L],nums[R] = nums[R],nums[L]
        return nums