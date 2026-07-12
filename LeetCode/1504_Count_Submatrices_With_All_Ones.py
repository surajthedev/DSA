# Given an m x n binary matrix mat, return the number of submatrices that have all ones.
# 
# Example 1:
# Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2.
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# 
# Example 2:
# Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# Output: 24
# 
# Constraints:
# 1 <= m, n <= 150
# mat[i][j] is either 0 or 1.

# Brute Force Solution
class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        
        for r1 in range(m):
            for c1 in range(n):
                for r2 in range(r1, m):
                    for c2 in range(c1, n):
                        all_ones = True
                        for i in range(r1, r2 + 1):
                            for j in range(c1, c2 + 1):
                                if mat[i][j] == 0:
                                    all_ones = False
                                    break
                            if not all_ones:
                                break
                        if all_ones:
                            count += 1
        return count

# Optimal Solution
class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] and j > 0:
                    mat[i][j] += mat[i][j - 1]
                    
        for i in range(m):
            for j in range(n):
                min_width = mat[i][j]
                for k in range(i, -1, -1):
                    if mat[k][j] == 0:
                        break
                    min_width = min(min_width, mat[k][j])
                    res += min_width
                    
        return res
