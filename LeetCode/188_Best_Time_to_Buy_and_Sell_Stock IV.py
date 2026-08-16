# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

# Constraints:

# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000






# Brute force:
from functools import lru_cache

class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)

        @lru_cache(None)
        def dp(day, transactions_left, holding):

            # Saare days khatam
            if day == n:
                return 0

            # Kuch nahi karna
            profit = dp(day + 1, transactions_left, holding)

            if holding:
                # Stock sell karo
                sell = prices[day] + dp(
                    day + 1,
                    transactions_left - 1,
                    0
                )

                profit = max(profit, sell)

            elif transactions_left > 0:
                # Stock buy karo
                buy = -prices[day] + dp(
                    day + 1,
                    transactions_left,
                    1
                )

                profit = max(profit, buy)

            return profit

        return dp(0, k, 0)












# Optimal:
class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0

        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:

            for t in range(1, k + 1):
                buy[t] = max(
                    buy[t],
                    sell[t - 1] - price
                )

                sell[t] = max(
                    sell[t],
                    buy[t] + price
                )

        return sell[k]