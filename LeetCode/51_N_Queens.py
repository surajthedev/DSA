# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9



# Brute Force:
class Solution:
    def solveNQueens(self, n: int):
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def isSafe(row, col):
            # Check same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check left upper diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check right upper diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        backtrack(0)
        return ans






# Optimal:
class Solution:
    def solveNQueens(self, n: int):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        cols = set()
        diag = set()       # row - col
        antiDiag = set()   # row + col

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                if col in cols:
                    continue

                if (row - col) in diag:
                    continue

                if (row + col) in antiDiag:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diag.add(row - col)
                antiDiag.add(row + col)

                backtrack(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                diag.remove(row - col)
                antiDiag.remove(row + col)

        backtrack(0)
        return ans