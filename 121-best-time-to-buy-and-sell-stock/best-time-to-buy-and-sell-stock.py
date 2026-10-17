class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_value = 10000000
        n = len(prices)
        diff = 0
        for i in range(0,len(prices)):
            min_value = min(min_value,prices[i])
            diff = max(diff,prices[i]-min_value)
        return diff
        