class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr, profit = 0, 0
        buy = prices[curr]
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            curr = prices[i] - buy
            profit = max(profit, curr)
        return profit
            


