# You are given an m x n binary matrix grid.

# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score after making any number of moves (including zero moves).



# Example 1:


# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# Example 2:

# Input: grid = [[0]]
# Output: 1


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
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
# Brute force:
class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for mask in range(1 << (m + n)):
            mat = [row[:] for row in grid]

            # Toggle rows
            for i in range(m):
                if mask & (1 << i):
                    for j in range(n):
                        mat[i][j] ^= 1

            # Toggle columns
            for j in range(n):
                if mask & (1 << (m + j)):
                    for i in range(m):
                        mat[i][j] ^= 1

            score = 0
            for row in mat:
                num = 0
                for bit in row:
                    num = num * 2 + bit
                score += num

            ans = max(ans, score)

        return ans










# Optimal:
class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Make first column all 1s by flipping rows
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        # For every column, maximize number of 1s
        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            zeros = m - ones

            if zeros > ones:
                for i in range(m):
                    grid[i][j] ^= 1

        # Calculate score
        ans = 0

        for i in range(m):
            num = 0
            for j in range(n):
                num = num * 2 + grid[i][j]
            ans += num

        return ans
