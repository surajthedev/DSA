# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 1. Each of the digits 1-9 must occur exactly once in each row.
# 2. Each of the digits 1-9 must occur exactly once in each column.
# 3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# 
# The '.' character indicates empty cells.
# 
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

# Brute Force Solution
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, k):
            for i in range(9):
                if board[r][i] == k:
                    return False
                if board[i][c] == k:
                    return False
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k:
                    return False
            return True
            
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for k in range(1, 10):
                            if is_valid(r, c, str(k)):
                                board[r][c] = str(k)
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True
            
        solve()

# Optimal Solution
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # A more optimal solution uses sets/arrays to keep track of used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)
                    
        def backtrack(idx=0):
            if idx == len(empty_cells):
                return True
                
            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + c // 3
            
            for val in map(str, range(1, 10)):
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    if backtrack(idx + 1):
                        return True
                        
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
                    
            return False
            
        backtrack()
