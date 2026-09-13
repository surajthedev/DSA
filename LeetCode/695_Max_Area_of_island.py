# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.










# Brute Force
class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        visited = set()
        ans = 0

        def dfs(r, c):
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))

            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        return ans









# Optimal
class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = 0
                    stack = [(r, c)]
                    grid[r][c] = 0

                    while stack:
                        x, y = stack.pop()
                        area += 1

                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x + dx, y + dy

                            if (
                                0 <= nx < m and
                                0 <= ny < n and
                                grid[nx][ny] == 1
                            ):
                                grid[nx][ny] = 0
                                stack.append((nx, ny))

                    ans = max(ans, area)

        return ans