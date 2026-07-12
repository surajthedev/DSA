# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# 
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# 
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# Brute Force Solution
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                    
        for j in range(9):
            col_set = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col_set:
                        return False
                    col_set.add(board[i][j])
                    
        for box_i in range(3):
            for box_j in range(3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_i*3 + i][box_j*3 + j]
                        if val != '.':
                            if val in box_set:
                                return False
                            box_set.add(val)
                            
        return True

# Optimal Solution
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]
        return len(res) == len(set(res))
