class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price, sell_price = prices[0], prices[0]
        buy_index, sell_index = 0, 0
        for i in range(len(prices)):
            price = prices[i]
            if price < buy_price:
                buy_price = price
                buy_index = i
            if price - buy_price > max_profit:
                sell_price = price
                sell_index = i
                max_profit = price - buy_price

        return max_profit