# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
# 
# Example 1:
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# 
# Example 2:
# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
# 
# Constraints:
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

# Brute Force Solution
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                max_k = min(m - i, n - j)
                for k in range(1, max_k + 1):
                    is_square = True
                    for r in range(i, i + k):
                        for c in range(j, j + k):
                            if matrix[r][c] == 0:
                                is_square = False
                                break
                        if not is_square:
                            break
                    if is_square:
                        count += 1
                    else:
                        break # If size k fails, size k+1 will also fail
        return count

# Optimal Solution
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                        res += matrix[i][j]
                        
        return res
