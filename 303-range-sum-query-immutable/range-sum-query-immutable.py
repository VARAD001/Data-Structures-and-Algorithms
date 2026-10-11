class NumArray:

    def __init__(self, nums: list[int]):
        self.arr = tuple(nums)
        self.prefix = [0] + []*len(nums)
        self.prefix_sum(self.arr)
    
    def prefix_sum(self,nums):
        a = 0
        for i in nums:
            a += i
            self.prefix.append(a)
    
    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix[right + 1] - self.prefix[left])
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)