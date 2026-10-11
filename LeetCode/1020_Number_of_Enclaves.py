# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.



# Example 1:


# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
# Example 2:


# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
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
# ### Brute Force — DFS

python
```

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r >= m or c < 0 or c >= n
                    or grid[r][c] == 0 or (r, c) in visited):
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans += 1

        return ans
```

### Optimal — BFS

python
```

from collections import deque

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in (0, n - 1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0

        for j in range(n):
            for i in (0, m - 1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                        and grid[nr][nc] == 1):
                    grid[nr][nc] = 0
                    q.append((nr, nc))

        return sum(sum(row) for row in grid)
```
