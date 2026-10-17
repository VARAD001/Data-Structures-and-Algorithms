class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        L = 0
        diff = 0
        for R in range(1,len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                diff= max(diff,prices[R] - prices[L])
        return diff
        