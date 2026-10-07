# You are given an m x n integer array grid where grid[i][j] could be:

# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



# Example 1:


# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:


# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:


# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# 1 <= m * n <= 20
# -1 <= grid[i][j] <= 2
# There is exactly one starting cell and one ending cell.
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
# Brute force:
class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        start = None
        empty = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    empty += 1
                elif grid[i][j] == 0:
                    empty += 1

        ans = 0

        def dfs(r, c, count):
            nonlocal ans

            if grid[r][c] == 2:
                if count == empty:
                    ans += 1
                return

            temp = grid[r][c]
            grid[r][c] = -1

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] in (0, 2):
                        dfs(nr, nc, count + 1)

            grid[r][c] = temp

        dfs(start[0], start[1], 1)

        return ans















# Optimal:
class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        cells = []
        start = end = -1

        for r in range(m):
            for c in range(n):
                if grid[r][c] != -1:
                    idx = len(cells)
                    cells.append((r, c))

                    if grid[r][c] == 1:
                        start = idx
                    elif grid[r][c] == 2:
                        end = idx

        k = len(cells)

        index = {pos: i for i, pos in enumerate(cells)}

        neighbors = [[] for _ in range(k)]

        for i, (r, c) in enumerate(cells):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (nr, nc) in index:
                    neighbors[i].append(index[(nr, nc)])

        full_mask = (1 << k) - 1
        memo = {}

        def dfs(pos, mask):
            if pos == end:
                return 1 if mask == full_mask else 0

            key = (pos, mask)

            if key in memo:
                return memo[key]

            ans = 0

            for nxt in neighbors[pos]:
                if not (mask & (1 << nxt)):
                    ans += dfs(nxt, mask | (1 << nxt))

            memo[key] = ans
            return ans

        return dfs(start, 1 << start)
