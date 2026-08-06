# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


# Brute Force:
class Solution:
    def searchMatrix(self, matrix, target):

        for row in matrix:

            if row[0] <= target <= row[-1]:

                for num in row:
                    if num == target:
                        return True

        return False






# Optimized Solution:
class Solution:
    def searchMatrix(self, matrix, target):

        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1

        while low <= high:

            mid = (low + high) // 2

            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False