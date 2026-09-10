# Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

# The height of the tree is height and the number of rows m should be equal to height + 1.
# The number of columns n should be equal to 2height+1 - 1.
# Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
# For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
# Continue this process until all the nodes in the tree have been placed.
# Any empty cells should contain the empty string "".
# Return the constructed matrix res.

 

# Example 1:


# Input: root = [1,2]
# Output: 
# [["","1",""],
#  ["2","",""]]
# Example 2:


# Input: root = [1,2,3,null,4]
# Output: 
# [["","","","1","","",""],
#  ["","2","","","","3",""],
#  ["","","4","","","",""]]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 210].
# -99 <= Node.val <= 99
# The depth of the tree will be in the range [1, 10].







# Brute force:
# Brute Force
class Solution:
    def printTree(self, root):
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        m = h + 1
        n = 2 ** (h + 1) - 1

        res = [[""] * n for _ in range(m)]

        def dfs(node, r, c):
            if not node:
                return

            res[r][c] = str(node.val)

            if r < h:
                offset = 2 ** (h - r - 1)
                dfs(node.left, r + 1, c - offset)
                dfs(node.right, r + 1, c + offset)

        dfs(root, 0, (n - 1) // 2)

        return res












# Optimal:
# Optimal - O(n)
class Solution:
    def printTree(self, root):
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)
        rows = height
        cols = 2 ** height - 1

        res = [[""] * cols for _ in range(rows)]

        def dfs(node, row, left, right):
            if not node:
                return

            mid = (left + right) // 2
            res[row][mid] = str(node.val)

            dfs(node.left, row + 1, left, mid - 1)
            dfs(node.right, row + 1, mid + 1, right)

        dfs(root, 0, 0, cols - 1)

        return res