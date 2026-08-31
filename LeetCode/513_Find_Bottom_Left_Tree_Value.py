# Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

# Example 1:


# Input: root = [2,1,3]
# Output: 1
# Example 2:


# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1







# Brute force:
class Solution:
    def findBottomLeftValue(self, root):
        levels = []

        def dfs(node, level):
            if not node:
                return

            if level == len(levels):
                levels.append([])

            levels[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return levels[-1][0]







# Optimal:
from collections import deque

class Solution:
    def findBottomLeftValue(self, root):
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return node.val