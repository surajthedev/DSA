# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100




# Brute force:
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        max_depth = 0

        def dfs(node, depth):
            nonlocal max_depth

            if not node:
                return

            depth += 1

            # Leaf node
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
                return

            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)

        return max_depth







# Optimal:
from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth