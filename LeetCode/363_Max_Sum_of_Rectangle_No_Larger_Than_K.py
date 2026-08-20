# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

# It is guaranteed that there will be a rectangle with a sum no larger than k.

 

# Example 1:


# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
# Example 2:

# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -105 <= k <= 105







# Brute force:
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])

        # Build prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    matrix[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        ans = float("-inf")

        # Choose top-left corner
        for r1 in range(m):
            for c1 in range(n):

                # Choose bottom-right corner
                for r2 in range(r1 + 1, m + 1):
                    for c2 in range(c1 + 1, n + 1):

                        total = (
                            prefix[r2][c2]
                            - prefix[r1][c2]
                            - prefix[r2][c1]
                            + prefix[r1][c1]
                        )

                        if total <= k:
                            ans = max(ans, total)

        return ans









# Optimal:
from bisect import bisect_left, insort


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])

        # We want fewer row pairs if possible
        if m > n:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m

        ans = float("-inf")

        for top in range(m):

            # Column sums between top and bottom
            col_sum = [0] * n

            for bottom in range(top, m):

                # Add current row to column sums
                for col in range(n):
                    col_sum[col] += matrix[bottom][col]

                # Find max subarray sum <= k
                prefix = 0
                sorted_prefix = [0]

                for value in col_sum:
                    prefix += value

                    # Need previous prefix >= prefix - k
                    pos = bisect_left(
                        sorted_prefix,
                        prefix - k
                    )

                    if pos < len(sorted_prefix):
                        current_sum = prefix - sorted_prefix[pos]
                        ans = max(ans, current_sum)

                        if ans == k:
                            return k

                    insort(sorted_prefix, prefix)

        return ans