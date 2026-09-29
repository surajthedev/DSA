# You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

# You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

# Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

# Return the minimum number of moves that you need to determine with certainty what the value of f is.



# Example 1:

# Input: k = 1, n = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1. If it breaks, we know that f = 0.
# Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
# If it does not break, then we know f = 2.
# Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
# Example 2:

# Input: k = 2, n = 6
# Output: 3
# Example 3:

# Input: k = 3, n = 14
# Output: 4


# Constraints:

# 1 <= k <= 100
# 1 <= n <= 104
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Brute Force - O(k * n^2 * moves)
class Solution:
    def superEggDrop(self, k, n):
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for floors in range(n + 1):
            dp[1][floors] = floors

        for eggs in range(2, k + 1):
            for floors in range(1, n + 1):
                dp[eggs][floors] = floors

                for x in range(1, floors + 1):
                    broken = dp[eggs - 1][x - 1]
                    not_broken = dp[eggs][floors - x]

                    dp[eggs][floors] = min(
                        dp[eggs][floors],
                        1 + max(broken, not_broken)
                    )

        return dp[k][n]













# Optimal - O(k * log n) approximately
# dp[e] = maximum number of floors that can be tested
# with e eggs and current number of moves.
class Solution:
    def superEggDrop(self, k, n):
        dp = [0] * (k + 1)
        moves = 0

        while dp[k] < n:
            moves += 1

            for eggs in range(k, 0, -1):
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1

        return moves
