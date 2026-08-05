# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200


# Brute Force Code:
class Solution:
    def minPathSum(self, grid):

        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):

            if i >= m or j >= n:
                return float('inf')

            if i == m - 1 and j == n - 1:
                return grid[i][j]

            down = dfs(i + 1, j)
            right = dfs(i, j + 1)

            return grid[i][j] + min(down, right)

        return dfs(0, 0)



# Optimal Code:
class Solution:
    def minPathSum(self, grid):

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # First Row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # First Column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Remaining Cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j],
                                            dp[i][j - 1])

        return dp[m - 1][n - 1]