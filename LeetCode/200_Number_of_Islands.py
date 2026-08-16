# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.








# Brute force:
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if grid[r][c] == "0":
                return

            # Mark visited
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            for c in range(n):

                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands










# Optimal:
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)

        return ans