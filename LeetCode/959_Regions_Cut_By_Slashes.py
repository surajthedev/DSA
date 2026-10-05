# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

# Given the grid grid represented as a string array, return the number of regions.

# Note that backslash characters are escaped, so a '\' is represented as '\\'.



# Example 1:


# Input: grid = [" /","/ "]
# Output: 2
# Example 2:


# Input: grid = [" /","  "]
# Output: 1
# Example 3:


# Input: grid = ["/\\","\\/"]
# Output: 5
# Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.


# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 30
# grid[i][j] is either '/', '\', or ' '.
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
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = n * 3
        board = [[0] * size for _ in range(size)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == '/':
                    board[r * 3][c * 3 + 2] = 1
                    board[r * 3 + 1][c * 3 + 1] = 1
                    board[r * 3 + 2][c * 3] = 1
                elif grid[r][c] == '\\':
                    board[r * 3][c * 3] = 1
                    board[r * 3 + 1][c * 3 + 1] = 1
                    board[r * 3 + 2][c * 3 + 2] = 1

        regions = 0

        def dfs(r, c):
            if r < 0 or r >= size or c < 0 or c >= size:
                return
            if board[r][c] != 0:
                return

            board[r][c] = 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(size):
            for c in range(size):
                if board[r][c] == 0:
                    regions += 1
                    dfs(r, c)

        return regions














# Optimal:
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = n * 3
        board = [[0] * size for _ in range(size)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == '/':
                    board[r * 3][c * 3 + 2] = 1
                    board[r * 3 + 1][c * 3 + 1] = 1
                    board[r * 3 + 2][c * 3] = 1

                elif grid[r][c] == '\\':
                    board[r * 3][c * 3] = 1
                    board[r * 3 + 1][c * 3 + 1] = 1
                    board[r * 3 + 2][c * 3 + 2] = 1

        def dfs(r, c):
            if r < 0 or r >= size or c < 0 or c >= size:
                return
            if board[r][c] == 1:
                return

            board[r][c] = 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        regions = 0

        for r in range(size):
            for c in range(size):
                if board[r][c] == 0:
                    regions += 1
                    dfs(r, c)

        return regions
