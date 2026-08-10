# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
 

# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000




# Brute force:
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        # Leaf node
        if root.left is None and root.right is None:
            return 1

        # Only right child exists
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # Only left child exists
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # Both children exist
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )







# Optimal:
from collections import deque

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # First leaf = minimum depth
            if node.left is None and node.right is None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))