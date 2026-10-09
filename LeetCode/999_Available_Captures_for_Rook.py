# You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

# A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

# Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

# Return the number of pawns the white rook is attacking.



# Example 1:


# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

# Output: 3

# Explanation:

# In this example, the rook is attacking all the pawns.

# Example 2:


# Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

# Output: 0

# Explanation:

# The bishops are blocking the rook from attacking any of the pawns.

# Example 3:


# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

# Output: 3

# Explanation:

# The rook is attacking the pawns at positions b5, d6, and f5.



# Constraints:

# board.length == 8
# board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'













### Brute Force

python
```

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        r = c = 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j

        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            i, j = r + dr, c + dc

            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] == 'B':
                    break
                if board[i][j] == 'p':
                    count += 1
                    break

                i += dr
                j += dc

        return count
```

### Optimal — O(1) Time, O(1) Space

python
```

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break

        count = 0

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i, j = r + dr, c + dc

            while 0 <= i < 8 and 0 <= j < 8:
                if board[i][j] != '.':
                    if board[i][j] == 'p':
                        count += 1
                    break

                i += dr
                j += dc

        return count
```
