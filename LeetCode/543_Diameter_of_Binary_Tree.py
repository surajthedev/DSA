# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100







# Brute force:
class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def diameter(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            return max(
                left_height + right_height,
                diameter(node.left),
                diameter(node.right)
            )

        return diameter(root)








# Optimal:
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.ans