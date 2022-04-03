class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price-min_price
            min_price = min(price,min_price)
            max_profit = max(max_profit,profit)
        return max_profit