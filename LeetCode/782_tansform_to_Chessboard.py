# You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.

# Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.

# A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

 

# Example 1:


# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation: One potential sequence of moves is shown.
# The first move swaps the first and second column.
# The second move swaps the second and third row.
# Example 2:


# Input: board = [[0,1],[1,0]]
# Output: 0
# Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
# Example 3:


# Input: board = [[1,0],[1,0]]
# Output: -1
# Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
 

# Constraints:

# n == board.length
# n == board[i].length
# 2 <= n <= 30
# board[i][j] is either 0 or 1.











# Optimal:
class Solution:
    def movesToChessboard(self, board):
        n = len(board)

        # Check whether board can be transformed into chessboard
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        # Count 1s in first row and first column
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))

        # Valid number of 1s
        if not (n // 2 <= row_sum <= (n + 1) // 2):
            return -1

        if not (n // 2 <= col_sum <= (n + 1) // 2):
            return -1

        # Calculate row moves
        row_moves = 0
        for i in range(n):
            if board[i][0] != i % 2:
                row_moves += 1

        # Calculate column moves
        col_moves = 0
        for j in range(n):
            if board[0][j] != j % 2:
                col_moves += 1

        # For odd n, starting bit is fixed by majority
        if n % 2 == 1:
            if row_moves % 2:
                row_moves = n - row_moves

            if col_moves % 2:
                col_moves = n - col_moves

        else:
            row_moves = min(row_moves, n - row_moves)
            col_moves = min(col_moves, n - col_moves)

        return (row_moves + col_moves) // 2