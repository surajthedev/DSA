# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.





# Brute force:
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, index):

            if index == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[index]:
                return False

            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Backtrack
            board[r][c] = temp

            return found

        for word in words:

            found = False

            for r in range(rows):
                for c in range(cols):

                    if board[r][c] == word[0]:
                        if dfs(r, c, 0):
                            found = True
                            break

                if found:
                    break

            if found:
                result.append(word)

        return result







# Optimal:
class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None


class Solution:

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        # -------------------------
        # Build Trie
        # -------------------------

        root = TrieNode()

        for word in words:
            curr = root

            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()

                curr = curr.children[ch]

            curr.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        # -------------------------
        # DFS + Backtracking
        # -------------------------

        def dfs(r, c, node):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            ch = board[r][c]

            if ch == '#' or ch not in node.children:
                return

            next_node = node.children[ch]

            # Complete word found
            if next_node.word is not None:
                result.append(next_node.word)

                # Prevent duplicate result
                next_node.word = None

            # Mark current cell as visited
            board[r][c] = '#'

            # Explore 4 directions
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # Backtrack
            board[r][c] = ch

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result