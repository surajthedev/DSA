# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 9


# Brute Force:
class Solution:
    def totalNQueens(self, n: int) -> int:

        board = [['.' for _ in range(n)] for _ in range(n)]
        count = 0

        def isSafe(row, col):

            # Same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):

                if isSafe(row, col):
                    board[row][col] = 'Q'

                    backtrack(row + 1)

                    board[row][col] = '.'

        backtrack(0)

        return count






# Optimal:
class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        diag = set()
        anti = set()

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):

                if col in cols:
                    continue

                if (row - col) in diag:
                    continue

                if (row + col) in anti:
                    continue

                cols.add(col)
                diag.add(row - col)
                anti.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag.remove(row - col)
                anti.remove(row + col)

        backtrack(0)

        return count