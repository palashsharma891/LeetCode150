class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        for sell in range(1, len(prices)):
            print(buy, sell)
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = i
                continue
            max_profit = max(max_profit, profit)
        return max_profit
