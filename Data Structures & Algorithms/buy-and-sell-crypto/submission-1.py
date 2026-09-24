class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for i in range(len(prices)):
            price = prices[i]
            if price < buy_price:
                buy_price = price
            if price - buy_price > max_profit:
                max_profit = price - buy_price

        return max_profit