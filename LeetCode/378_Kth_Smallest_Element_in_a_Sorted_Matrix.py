# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2





# Brute force:
class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        arr = []

        for row in matrix:
            for num in row:
                arr.append(num)

        arr.sort()

        return arr[k - 1]








# Optimal:
class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        def count_less_equal(x):
            row = n - 1
            col = 0
            count = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row + 1
                    col += 1
                else:
                    row -= 1

            return count

        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = left + (right - left) // 2

            if count_less_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left