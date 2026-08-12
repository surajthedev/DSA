# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.\





# Brute force:
from collections import deque

class Solution:
    def solve(self, board):
        m = len(board)
        n = len(board[0])

        visited = set()

        for r in range(m):
            for c in range(n):

                if board[r][c] != 'O' or (r, c) in visited:
                    continue

                # Current region
                queue = deque([(r, c)])
                visited.add((r, c))

                region = []
                surrounded = True

                while queue:
                    x, y = queue.popleft()
                    region.append((x, y))

                    # Boundary par hai?
                    if (
                        x == 0 or
                        x == m - 1 or
                        y == 0 or
                        y == n - 1
                    ):
                        surrounded = False

                    directions = [
                        (1, 0),
                        (-1, 0),
                        (0, 1),
                        (0, -1)
                    ]

                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        if (
                            0 <= nx < m and
                            0 <= ny < n and
                            board[nx][ny] == 'O' and
                            (nx, ny) not in visited
                        ):
                            visited.add((nx, ny))
                            queue.append((nx, ny))

                # Agar region completely surrounded hai
                if surrounded:
                    for x, y in region:
                        board[x][y] = 'X'









# Optimal:
class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            if (
                r < 0 or
                r >= m or
                c < 0 or
                c >= n or
                board[r][c] != 'O'
            ):
                return

            # Mark as safe
            board[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Boundary rows
        for c in range(n):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[m - 1][c] == 'O':
                dfs(m - 1, c)

        # 2. Boundary columns
        for r in range(m):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][n - 1] == 'O':
                dfs(r, n - 1)

        # 3. Capture surrounded regions
        for r in range(m):
            for c in range(n):

                if board[r][c] == 'O':
                    board[r][c] = 'X'

                elif board[r][c] == '#':
                    board[r][c] = 'O'