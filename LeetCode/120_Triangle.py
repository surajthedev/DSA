# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
 




# Brute force:
class Solution:
    def minimumTotal(self, triangle):
        def dfs(row, col):
            # Last row
            if row == len(triangle) - 1:
                return triangle[row][col]

            left = dfs(row + 1, col)
            right = dfs(row + 1, col + 1)

            return triangle[row][col] + min(left, right)

        return dfs(0, 0)







# Optimal:
class Solution:
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(
                    dp[col],
                    dp[col + 1]
                )

        return dp[0]