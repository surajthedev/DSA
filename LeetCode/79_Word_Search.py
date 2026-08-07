# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.



# Brute force:
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c, index):

            # Word complete
            if index == len(word):
                return True

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Already used
            if (r, c) in visited:
                return False

            # Character doesn't match
            if board[r][c] != word[index]:
                return False

            visited.add((r, c))

            # 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Backtrack
            visited.remove((r, c))

            return found

        # Har cell ko starting point try karo
        for r in range(rows):
            for c in range(cols):

                if dfs(r, c, 0):
                    return True

        return False






# Optimal solution:
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        # --------------------------------------------------
        # Frequency pruning
        # --------------------------------------------------

        board_count = {}

        for row in board:
            for ch in row:
                board_count[ch] = board_count.get(ch, 0) + 1

        word_count = {}

        for ch in word:
            word_count[ch] = word_count.get(ch, 0) + 1

        # Agar word ke kisi character ki frequency
        # board mein available hi nahi hai
        for ch, count in word_count.items():

            if board_count.get(ch, 0) < count:
                return False

        # --------------------------------------------------
        # Optional optimization:
        # Rare character se search start karo
        # --------------------------------------------------

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        # --------------------------------------------------
        # DFS + Backtracking
        # --------------------------------------------------

        def dfs(r, c, index):

            # Entire word found
            if index == len(word):
                return True

            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Character mismatch
            if board[r][c] != word[index]:
                return False

            # Mark current cell as visited
            original = board[r][c]
            board[r][c] = '#'

            # Explore 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Restore cell
            board[r][c] = original

            return found

        # --------------------------------------------------
        # Try every cell as starting point
        # --------------------------------------------------

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == word[0]:

                    if dfs(r, c, 0):
                        return True

        return False