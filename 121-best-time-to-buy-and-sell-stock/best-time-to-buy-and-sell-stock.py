class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        min_price = [0]*n
        dp = [0] * n
        min_price[0] = prices[0]
        for i in range(1,n):
            min_price[i] = min(min_price[i -1],prices[i])
            dp[i] = max(dp[i-1] , prices[i] - min_price[i])
        return dp[-1]