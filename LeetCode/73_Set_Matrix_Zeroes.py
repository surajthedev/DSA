# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1



# Brute Force:
class Solution:
    def setZeroes(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        MARK = None

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:

                    # Row
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = MARK

                    # Column
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = MARK

        for i in range(m):
            for j in range(n):
                if matrix[i][j] is MARK:
                    matrix[i][j] = 0








# Optimal:
class Solution:
    def setZeroes(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        col0 = 1

        for i in range(m):

            if matrix[i][0] == 0:
                col0 = 0

            for j in range(1, n):

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(m - 1, -1, -1):

            for j in range(n - 1, 0, -1):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if col0 == 0:
                matrix[i][0] = 0