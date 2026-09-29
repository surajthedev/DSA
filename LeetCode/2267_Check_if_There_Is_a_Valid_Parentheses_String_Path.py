# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

# The path starts from the upper left cell (0, 0).
# The path ends at the bottom-right cell (m - 1, n - 1).
# The path only ever moves down or right.
# The resulting parentheses string formed by the path is valid.
# Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.



# Example 1:


# Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
# Output: true
# Explanation: The above diagram shows two possible paths that form valid parentheses strings.
# The first path shown results in the valid parentheses string "()(())".
# The second path shown results in the valid parentheses string "((()))".
# Note that there may be other valid parentheses string paths.
# Example 2:


# Input: grid = [[")",")"],["(","("]]
# Output: false
# Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is either '(' or ')'.
#
#
#
#
#
#
#
#
#
#
# Brute Force - O(2^(m+n)):
class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c, balance):
            balance += 1 if grid[r][c] == '(' else -1

            if balance < 0:
                return False

            if r == m - 1 and c == n - 1:
                return balance == 0

            if r + 1 < m and dfs(r + 1, c, balance):
                return True

            if c + 1 < n and dfs(r, c + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)









# Optimal - O(m * n * (m + n)) Time, O(m * n * (m + n)) Space
class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        if (m + n - 1) % 2:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                if grid[r][c] == '(':
                    add = 1
                else:
                    add = -1

                if r > 0:
                    for balance in dp[r - 1][c]:
                        new_balance = balance + add
                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

                if c > 0:
                    for balance in dp[r][c - 1]:
                        new_balance = balance + add
                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

        return 0 in dp[-1][-1]
