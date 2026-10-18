class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        L = 0
        total = 0
        for R in range(len(prices)-1):
            if prices[R + 1] <  prices[R]:
                total += prices[R]-prices[L]
                L = R + 1
        total += max(0,prices[-1]-prices[L])
        return total