class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum = 0
        x = 0
        num = str(n)
        for i in num:
            sum += int(i)
            x = (10*x) + int(i) if int(i) != 0 else x
        return sum*x
        