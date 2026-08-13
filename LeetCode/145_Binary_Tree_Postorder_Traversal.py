# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 






# Brute force:
class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            # Left
            dfs(node.left)

            # Right
            dfs(node.right)

            # Root
            result.append(node.val)

        dfs(root)

        return result






# Optimal:
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            result.append(node.val)

            # Left first push
            if node.left:
                stack.append(node.left)

            # Right second push
            if node.right:
                stack.append(node.right)

        result.reverse()

        return result