# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20



# Brute Force:
class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]

        # Right, Down, Left, Up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        direction = 0
        row = 0
        col = 0

        for num in range(1, n * n + 1):
            matrix[row][col] = num
            visited[row][col] = True

            newRow = row + dr[direction]
            newCol = col + dc[direction]

            if (0 <= newRow < n and
                0 <= newCol < n and
                not visited[newRow][newCol]):

                row = newRow
                col = newCol
            else:
                direction = (direction + 1) % 4
                row += dr[direction]
                col += dc[direction]

        return matrix






# Optimal:
class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while left <= right and top <= bottom:

            # Left -> Right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # Top -> Bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix