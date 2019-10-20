"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""


class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        if not prices:
            return profit
        low = prices[0]
        for index in range(1, len(prices)):
            stock_price = prices[index]
            if stock_price < low:
                low = stock_price
            else:
                current_profit = stock_price - low
                if current_profit > profit:
                    profit = current_profit
        return profit

"""
Runtime: O(n)
"""
if __name__ == "__main__":
    lol = Solution()
    prices = []
    print(lol.maxProfit(prices))
