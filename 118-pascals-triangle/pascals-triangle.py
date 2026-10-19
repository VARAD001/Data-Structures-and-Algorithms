class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        new_layer = [1]
        for i in range(numRows-1):
            new_layer = self.make_layer(new_layer)
            result.append(new_layer)
        return result
        
    def make_layer(self,nums):
        res = []
        res.append(nums[0])
        for i in range(len(nums)-1):
            res.append(nums[i] + nums[i+1])
        res.append(nums[-1])
        return res