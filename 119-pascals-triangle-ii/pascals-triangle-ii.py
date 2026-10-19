class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(rowIndex):
            result = self.make_layer(result)
        return result

    def make_layer(self,nums):
        res = [1]
        for i in range(len(nums)-1):
            res.append(nums[i]+nums[i+1])
        res.append(1)
        return res
        