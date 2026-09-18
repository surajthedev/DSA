# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

# Example 1:


# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.# Brute Force

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            for c in range(n):
                value = matrix[r][c]

                i, j = r + 1, c + 1

                while i < m and j < n:
                    if matrix[i][j] != value:
                        return False
                    i += 1
                    j += 1

        return True















# Brute Force

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            for c in range(n):
                value = matrix[r][c]

                i, j = r + 1, c + 1

                while i < m and j < n:
                    if matrix[i][j] != value:
                        return False
                    i += 1
                    j += 1

        return True














# Optimal - O(m * n)

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False

        return True







