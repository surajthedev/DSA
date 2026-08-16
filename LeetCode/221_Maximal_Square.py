# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.






# Brute force:
class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    size = 1

                    while i + size <= m and j + size <= n:
                        valid = True

                        # Bottom row
                        for col in range(j, j + size):
                            if matrix[i + size - 1][col] == "0":
                                valid = False
                                break

                        # Right column
                        if valid:
                            for row in range(i, i + size):
                                if matrix[row][j + size - 1] == "0":
                                    valid = False
                                    break

                        if not valid:
                            break

                        max_side = max(max_side, size)
                        size += 1

        return max_side * max_side







# Optimal:
class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [0] * (n + 1)
        max_side = 0
        diagonal = 0

        for i in range(1, m + 1):
            diagonal = 0

            for j in range(1, n + 1):
                top = dp[j]

                if matrix[i - 1][j - 1] == "1":
                    dp[j] = 1 + min(
                        dp[j],
                        dp[j - 1],
                        diagonal
                    )

                    max_side = max(max_side, dp[j])

                else:
                    dp[j] = 0

                diagonal = top

        return max_side * max_side