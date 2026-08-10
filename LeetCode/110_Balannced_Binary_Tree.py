# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104







# Brute force:
class Solution:
    def isBalanced(self, root):

        if not root:
            return True

        def height(node):
            if not node:
                return 0

            return 1 + max(
                height(node.left),
                height(node.right)
            )

        left_height = height(root.left)
        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return (
            self.isBalanced(root.left)
            and
            self.isBalanced(root.right)
        )








# Optimal:
class Solution:
    def isBalanced(self, root):

        def dfs(node):

            # Empty tree balanced hai
            if not node:
                return 0

            left_height = dfs(node.left)

            # Left subtree unbalanced
            if left_height == -1:
                return -1

            right_height = dfs(node.right)

            # Right subtree unbalanced
            if right_height == -1:
                return -1

            # Current node par balance check
            if abs(left_height - right_height) > 1:
                return -1

            # Current subtree ki height
            return 1 + max(left_height, right_height)

        return dfs(root) != -1