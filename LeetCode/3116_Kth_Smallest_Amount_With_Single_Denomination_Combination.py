# You are given an integer array coins representing coins of different denominations and an integer k.

# You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

# Return the kth smallest amount that can be made using these coins.

 

# Example 1:

# Input: coins = [3,6,9], k = 3

# Output: 9

# Explanation: The given coins can make the following amounts:
# Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
# Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
# Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
# All of the coins combined produce: 3, 6, 9, 12, 15, etc.

# Example 2:

# Input: coins = [5,2], k = 7

# Output: 12

# Explanation: The given coins can make the following amounts:
# Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
# Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
# All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

 

# Constraints:

# 1 <= coins.length <= 15
# 1 <= coins[i] <= 25
# 1 <= k <= 2 * 109
# coins contains pairwise distinct integers.






# Brute force:
class Solution:
    def findKthSmallest(self, coins, k):
        amount = 1
        count = 0

        while count < k:
            for coin in coins:
                if amount % coin == 0:
                    count += 1
                    break

            amount += 1

        return amount - 1






# Optimal:
from math import gcd


class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """
            Number of unique positive integers <= x
            that are divisible by at least one coin.
            """
            total = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])

                        # No multiple of current_lcm <= x
                        if current_lcm > x:
                            break

                if current_lcm > x:
                    continue

                if bits % 2 == 1:
                    total += x // current_lcm
                else:
                    total -= x // current_lcm

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = left + (right - left) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left