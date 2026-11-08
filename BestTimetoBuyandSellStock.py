class Solution:
    def maxProfit(self, prices):

        min_price = float('inf')
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            else:
                profit = price - min_price

                if profit > max_profit:
                    max_profit = profit

        return max_profit
    
    
class solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit