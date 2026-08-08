# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= rows, cols <= 200
# matrix[i][j] is '0' or '1'.


# Optimal:
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for r in range(rows):

            # Build histogram
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Largest rectangle in histogram
            stack = []

            for c in range(cols + 1):

                # Sentinel 0 at the end
                current_height = heights[c] if c < cols else 0

                while stack and heights[stack[-1]] > current_height:
                    h = heights[stack.pop()]

                    if stack:
                        width = c - stack[-1] - 1
                    else:
                        width = c

                    max_area = max(max_area, h * width)

                stack.append(c)

        return max_area