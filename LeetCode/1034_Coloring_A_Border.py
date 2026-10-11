# You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

# Two squares are called adjacent if they are next to each other in any of the 4 directions.

# Two squares belong to the same connected component if they have the same color and they are adjacent.

# The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

# You should color the border of the connected component that contains the square grid[row][col] with color.

# Return the final grid.



# Example 1:

# Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# Output: [[3,3],[3,2]]
# Example 2:

# Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# Output: [[1,3,3],[2,3,3]]
# Example 3:

# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# Output: [[2,2,2],[2,1,2],[2,2,2]]


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j], color <= 1000
# 0 <= row < m
# 0 <= col < n
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
# ### Brute Force (DFS)

python
```
class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        original = grid[row][col]
        visited = set()
        border = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            visited.add((r, c))
            is_border = False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    is_border = True
                elif grid[nr][nc] != original:
                    is_border = True
                elif (nr, nc) not in visited:
                    dfs(nr, nc)

            if is_border:
                border.append((r, c))

        dfs(row, col)

        for r, c in border:
            grid[r][c] = color

        return grid
```

### Optimal (BFS)

python
```
from collections import deque

class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        original = grid[row][col]
        visited = {(row, col)}
        queue = deque([(row, col)])
        border = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            is_border = False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    is_border = True
                elif grid[nr][nc] != original:
                    is_border = True
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

            if is_border:
                border.append((r, c))

        for r, c in border:
            grid[r][c] = color

        return grid
```
