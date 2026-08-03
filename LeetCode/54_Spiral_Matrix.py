# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


# Brute Force:
class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])

        visited = [[False] * n for _ in range(m)]

        ans = []

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        d = 0
        r = c = 0

        for _ in range(m * n):
            ans.append(matrix[r][c])
            visited[r][c] = True

            nr = r + dirs[d][0]
            nc = c + dirs[d][1]

            if (0 <= nr < m and
                0 <= nc < n and
                not visited[nr][nc]):

                r = nr
                c = nc
            else:
                d = (d + 1) % 4
                r += dirs[d][0]
                c += dirs[d][1]

        return ans





# Optimal:
class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        ans = []

        while top <= bottom and left <= right:

            # Left -> Right
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1

            # Top -> Bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Right -> Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans