# Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

# The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares ' '.
# The first player always places 'X' characters, while the second player always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
 

# Example 1:


# Input: board = ["O  ","   ","   "]
# Output: false
# Explanation: The first player always plays "X".
# Example 2:


# Input: board = ["XOX"," X ","   "]
# Output: false
# Explanation: Players take turns making moves.
# Example 3:


# Input: board = ["XOX","O O","XOX"]
# Output: true
 

# Constraints:

# board.length == 3
# board[i].length == 3
# board[i][j] is either 'X', 'O', or ' '.












# Brute Force
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = sum(row.count('X') for row in board)
        o = sum(row.count('O') for row in board)

        def win(p):
            for i in range(3):
                if all(board[i][j] == p for j in range(3)):
                    return True
                if all(board[j][i] == p for j in range(3)):
                    return True

            return (
                all(board[i][i] == p for i in range(3)) or
                all(board[i][2 - i] == p for i in range(3))
            )

        x_win = win('X')
        o_win = win('O')

        if x < o or x > o + 1:
            return False

        if x_win and o_win:
            return False

        if x_win and x != o + 1:
            return False

        if o_win and x != o:
            return False

        return True










# Optimal
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = sum(row.count('X') for row in board)
        o = sum(row.count('O') for row in board)

        def win(p):
            lines = [
                board[0], board[1], board[2],
                ''.join(board[i][0] for i in range(3)),
                ''.join(board[i][1] for i in range(3)),
                ''.join(board[i][2] for i in range(3)),
                ''.join(board[i][i] for i in range(3)),
                ''.join(board[i][2 - i] for i in range(3))
            ]
            return p * 3 in lines

        if x != o and x != o + 1:
            return False

        x_win = win('X')
        o_win = win('O')

        if x_win and x != o + 1:
            return False

        if o_win and x != o:
            return False

        if x_win and o_win:
            return False

        return True