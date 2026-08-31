# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:

# Input: root = [1,2,3]
# Output: [1,3]
 

# Constraints:

# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1







# Brute force:
class Solution:
    def largestValues(self, root):
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

        return [max(level) for level in levels]









# Optimal:
from collections import deque

class Solution:
    def largestValues(self, root):
        if not root:
            return []

        queue = deque([root])
        answer = []

        while queue:
            max_value = float('-inf')

            for _ in range(len(queue)):
                node = queue.popleft()

                max_value = max(max_value, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            answer.append(max_value)

        return answer