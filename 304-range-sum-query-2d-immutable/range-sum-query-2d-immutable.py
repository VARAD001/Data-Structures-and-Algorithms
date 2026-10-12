class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefix = self.prefix_sum(matrix)
        
    def prefix_sum(self,nums):
        prefix = []
        for rows in nums:
            new = []
            a = 0
            for cols in rows:
                a += cols
                new.append(a)
            prefix.append([0]+new)
        return prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row in range(row1,row2+1):
            ans += (self.prefix[row][col2+1]-self.prefix[row][col1])
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)