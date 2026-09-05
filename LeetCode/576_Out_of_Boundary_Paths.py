# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:


# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:


# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
 

# Constraints:

# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n







# Brute force:
class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7

        def dfs(r, c, moves):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            if moves == 0:
                return 0

            return (
                dfs(r + 1, c, moves - 1)
                + dfs(r - 1, c, moves - 1)
                + dfs(r, c + 1, moves - 1)
                + dfs(r, c - 1, moves - 1)
            ) % MOD

        return dfs(startRow, startColumn, maxMove)








# Optimal:
class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7

        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        ans = 0

        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]

            for r in range(m):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue

                    if r == 0:
                        ans += dp[r][c]
                    else:
                        new_dp[r - 1][c] += dp[r][c]

                    if r == m - 1:
                        ans += dp[r][c]
                    else:
                        new_dp[r + 1][c] += dp[r][c]

                    if c == 0:
                        ans += dp[r][c]
                    else:
                        new_dp[r][c - 1] += dp[r][c]

                    if c == n - 1:
                        ans += dp[r][c]
                    else:
                        new_dp[r][c + 1] += dp[r][c]

            dp = new_dp
            ans %= MOD

        return ans