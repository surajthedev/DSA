# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1





# Brute force:
class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):
            best = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    matrix[nr][nc] > matrix[r][c]):

                    best = max(
                        best,
                        1 + dfs(nr, nc)
                    )

            return best

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans






# Optimal:
class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        memo = [[0] * n for _ in range(m)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]

            best = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    matrix[nr][nc] > matrix[r][c]):

                    best = max(
                        best,
                        1 + dfs(nr, nc)
                    )

            memo[r][c] = best
            return best

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans