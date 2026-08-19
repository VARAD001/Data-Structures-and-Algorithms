class Solution:
    def climbStairs(self, n: int) -> int:
        liz = [0]*(n+2)
        liz[1] = 1
        liz[2] = 2
        for i in range(3, n+1):
            liz[i] = liz[i-1] + liz[i-2]
        return liz[n]
        