# You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through, or
# -1 means the cell contains a thorn that blocks your way.
# Return the maximum number of cherries you can collect by following the rules below:

# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
 

# Example 1:


# Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# Output: 5
# Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more cherry.
# The total number of cherries picked up is 5, and this is the maximum possible.
# Example 2:

# Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Output: 0
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# grid[i][j] is -1, 0, or 1.
# grid[0][0] != -1
# grid[n - 1][n - 1] != -1










# Brute force:
class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        memo = {}

        def dfs(r1, c1, r2, c2):
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return -10**9

            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -10**9

            if (r1, c1, r2, c2) in memo:
                return memo[(r1, c1, r2, c2)]

            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            cherries = grid[r1][c1]

            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            best = max(
                dfs(r1 + 1, c1, r2 + 1, c2),
                dfs(r1 + 1, c1, r2, c2 + 1),
                dfs(r1, c1 + 1, r2 + 1, c2),
                dfs(r1, c1 + 1, r2, c2 + 1)
            )

            memo[(r1, c1, r2, c2)] = cherries + best
            return memo[(r1, c1, r2, c2)]

        ans = dfs(0, 0, 0, 0)
        return max(0, ans)









# Optimal:
class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        NEG = -10**9

        dp = [[NEG] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for k in range(1, 2 * n - 1):
            new_dp = [[NEG] * n for _ in range(n)]

            r_min = max(0, k - (n - 1))
            r_max = min(n - 1, k)

            for r1 in range(r_min, r_max + 1):
                c1 = k - r1

                if grid[r1][c1] == -1:
                    continue

                for r2 in range(r_min, r_max + 1):
                    c2 = k - r2

                    if grid[r2][c2] == -1:
                        continue

                    best = dp[r1][r2]

                    if r1 > 0:
                        best = max(best, dp[r1 - 1][r2])

                    if r2 > 0:
                        best = max(best, dp[r1][r2 - 1])

                    if r1 > 0 and r2 > 0:
                        best = max(best, dp[r1 - 1][r2 - 1])

                    if best == NEG:
                        continue

                    cherries = grid[r1][c1]

                    if r1 != r2:
                        cherries += grid[r2][c2]

                    new_dp[r1][r2] = best + cherries

            dp = new_dp

        return max(0, dp[n - 1][n - 1])