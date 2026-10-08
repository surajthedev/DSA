# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
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
# ## Brute Force

```
class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        minutes = 0

        while True:
            rotten = []

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        rotten.append((i, j))

            changed = False

            for i, j in rotten:
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            changed = True

            if not changed:
                break

            minutes += 1

        for row in grid:
            if 1 in row:
                return -1

        return minutes
```

## Optimal — Multi-Source BFS

```
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            fresh -= 1
                            queue.append((ni, nj))

            minutes += 1

        return minutes if fresh == 0 else -1
```

**Complexity:**

- Brute Force: `O((m × n)²)` worst case
- Optimal BFS: `O(m × n)` time, `O(m × n)` space
