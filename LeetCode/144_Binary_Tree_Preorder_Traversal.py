# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100








# Brute force:
class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            # Root
            result.append(node.val)

            # Left
            dfs(node.left)

            # Right
            dfs(node.right)

        dfs(root)

        return result








# Optimal:
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            result.append(node.val)

            # Right first
            if node.right:
                stack.append(node.right)

            # Left second
            if node.left:
                stack.append(node.left)

        return result