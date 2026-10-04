# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.



# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1


# Constraints:

# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
#
#
#
#
#
#
#
#
#
# # Brute Force - DFS from every cell of the first island
class Solution:
    def shortestBridge(self, grid):
        n = len(grid)

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return

            grid[r][c] = 2
            first.append((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        first = []

        found = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        ans = float("inf")

        for r, c in first:
            for x in range(n):
                for y in range(n):
                    if grid[x][y] == 1:
                        ans = min(ans, abs(r - x) + abs(c - y) - 1)

        return ans







# Optimal - DFS + Multi-source BFS
from collections import deque

class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        q = deque()

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= n:
                return
            if grid[r][c] != 1:
                return

            grid[r][c] = 2
            q.append((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        found = False

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        steps = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue

                    if grid[nr][nc] == 1:
                        return steps

                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            steps += 1

        return -1
