# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
# 
# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# 
# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
# 
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# -10^5 <= mat[i][j] <= 10^5

# Brute Force Solution
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
            
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m + n - 1)]
        
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])
                
        res = []
        for i, diag in enumerate(diagonals):
            if i % 2 == 0:
                res.extend(diag[::-1])
            else:
                res.extend(diag)
                
        return res

# Optimal Solution
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
            
        m, n = len(mat), len(mat[0])
        res = []
        row, col = 0, 0
        direction = 1
        
        while len(res) < m * n:
            res.append(mat[row][col])
            if direction == 1:
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1
                    
        return res
