class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total = 0
        diff = 0
        mini = prices[0]
        for i in range(len(prices)-1):
            if prices[i]> prices[i+1]:
                diff = (prices[i]-mini)
                total += diff
                mini = prices[i+1]
        diff = (prices[-1]-mini)
        total += diff
        return total




