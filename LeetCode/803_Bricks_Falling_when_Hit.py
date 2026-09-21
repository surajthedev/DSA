# You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

# It is directly connected to the top of the grid, or
# At least one other brick in its four adjacent cells is stable.
# You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

# Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

# Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

 

# Example 1:

# Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# Output: [2]
# Explanation: Starting with the grid:
# [[1,0,0,0],
#  [1,1,1,0]]
# We erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
#  [0,1,1,0]]
# The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
# [[1,0,0,0],
#  [0,0,0,0]]
# Hence the result is [2].
# Example 2:

# Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# Output: [0,0]
# Explanation: Starting with the grid:
# [[1,0,0,0],
#  [1,1,0,0]]
# We erase the underlined brick at (1,1), resulting in the grid:
# [[1,0,0,0],
#  [1,0,0,0]]
# All remaining bricks are still stable, so no bricks fall. The grid remains the same:
# [[1,0,0,0],
#  [1,0,0,0]]
# Next, we erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
#  [0,0,0,0]]
# Once again, all remaining bricks are still stable, so no bricks fall.
# Hence the result is [0,0].
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] is 0 or 1.
# 1 <= hits.length <= 4 * 104
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# All (xi, yi) are unique.



















# Brute Force

class Solution:
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        result = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def mark_stable():
            stable = [[False] * n for _ in range(m)]
            stack = []

            for j in range(n):
                if grid[0][j] == 1:
                    stable[0][j] = True
                    stack.append((0, j))

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n and
                        grid[nr][nc] == 1 and not stable[nr][nc]):
                        stable[nr][nc] = True
                        stack.append((nr, nc))

            return stable

        for r, c in hits:
            if grid[r][c] == 0:
                result.append(0)
                continue

            grid[r][c] = 0
            stable = mark_stable()

            fallen = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not stable[i][j]:
                        grid[i][j] = 0
                        fallen += 1

            result.append(fallen)

        return result

















# Optimal - Reverse Process + Union Find

class Solution:
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        total = m * n
        roof = total

        parent = list(range(total + 1))
        size = [1] * (total + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        def index(r, c):
            return r * n + c

        original = [row[:] for row in grid]

        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    idx = index(r, c)

                    if r == 0:
                        union(idx, roof)

                    if r > 0 and grid[r - 1][c] == 1:
                        union(idx, index(r - 1, c))

                    if c > 0 and grid[r][c - 1] == 1:
                        union(idx, index(r, c - 1))

        result = [0] * len(hits)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]

            if original[r][c] == 0:
                continue

            before = size[find(roof)]

            grid[r][c] = 1
            idx = index(r, c)

            if r == 0:
                union(idx, roof)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    union(idx, index(nr, nc))

            after = size[find(roof)]

            result[i] = max(0, after - before - 1)

        return result