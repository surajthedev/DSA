# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return the number of maximum integers in the matrix after performing all the operations.

 

# Example 1:


# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
# Example 2:

# Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4
# Example 3:

# Input: m = 3, n = 3, ops = []
# Output: 9
 

# Constraints:

# 1 <= m, n <= 4 * 104
# 0 <= ops.length <= 104
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n







# Brute force:
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for a, b in ops:
            for i in range(a):
                for j in range(b):
                    matrix[i][j] += 1

        maximum = max(map(max, matrix))

        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == maximum:
                    count += 1

        return count






# Optimal:
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_a = m
        min_b = n

        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)

        return min_a * min_b