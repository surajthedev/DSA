# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 

# Constraints:

# 1 <= n <= 104





# Brute force:
class Solution:
    def numSquares(self, n):
        squares = []

        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        def solve(rem):
            if rem == 0:
                return 0

            ans = float('inf')

            for square in squares:
                if square > rem:
                    break

                ans = min(
                    ans,
                    1 + solve(rem - square)
                )

            return ans

        return solve(n)





# Optimal:
class Solution:
    def numSquares(self, n):
        squares = []

        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [0] + [float('inf')] * n

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break

                dp[i] = min(
                    dp[i],
                    dp[i - square] + 1
                )

        return dp[n]