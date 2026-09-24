# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.



# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.


# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
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
# Brute force:
class Solution:
    def largestIsland(self, grid):
        n = len(grid)

        def dfs(r, c, visited):
            if (r < 0 or r >= n or c < 0 or c >= n or
                grid[r][c] == 0 or (r, c) in visited):
                return 0

            visited.add((r, c))

            return (1 +
                    dfs(r + 1, c, visited) +
                    dfs(r - 1, c, visited) +
                    dfs(r, c + 1, visited) +
                    dfs(r, c - 1, visited))

        ans = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1

                    visited = set()
                    ans = max(ans, dfs(i, j, visited))

                    grid[i][j] = 0

        if ans == 0:
            return n * n

        return ans








# Optimal:
# class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        island_id = 2
        sizes = {}

        def dfs(r, c):
            if (r < 0 or r >= n or c < 0 or c >= n
                    or grid[r][c] != 1):
                return 0

            grid[r][c] = island_id
            size = 1

            for dr, dc in directions:
                size += dfs(r + dr, c + dc)

            return size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[island_id] = dfs(i, j)
                    island_id += 1

        ans = max(sizes.values(), default=0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    total = 1
                    seen = set()

                    for dr, dc in directions:
                        r, c = i + dr, j + dc

                        if (0 <= r < n and 0 <= c < n
                                and grid[r][c] > 1
                                and grid[r][c] not in seen):
                            seen.add(grid[r][c])
                            total += sizes[grid[r][c]]

                    ans = max(ans, total)

        return ans
