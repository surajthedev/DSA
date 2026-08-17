# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

 

# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.





# Brute force:
class Solution:
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])

        new_board = [[0] * n for _ in range(m)]

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(m):
            for c in range(n):

                live_neighbors = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        live_neighbors += board[nr][nc]

                if board[r][c] == 1:
                    if live_neighbors == 2 or live_neighbors == 3:
                        new_board[r][c] = 1
                else:
                    if live_neighbors == 3:
                        new_board[r][c] = 1

        # Original board update
        for r in range(m):
            for c in range(n):
                board[r][c] = new_board[r][c]







# Optimal:
class Solution:
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # First pass: determine next state
        for r in range(m):
            for c in range(n):

                live_neighbors = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        # 1 or 2 means OLD state was live
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1

                # Live cell
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2

                # Dead cell
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3

        # Second pass: convert temporary states
        for r in range(m):
            for c in range(n):

                if board[r][c] == 2:
                    board[r][c] = 0

                elif board[r][c] == 3:
                    board[r][c] = 1