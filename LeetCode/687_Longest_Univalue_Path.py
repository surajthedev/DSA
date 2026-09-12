# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).
# Example 2:


# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 4).
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.








# Brute force:
class Solution:
    def longestUnivaluePath(self, root):
        if not root:
            return 0

        def height(node, value):
            if not node or node.val != value:
                return 0

            return 1 + max(
                height(node.left, value),
                height(node.right, value)
            )

        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return

            left = height(node.left, node.val)
            right = height(node.right, node.val)

            ans = max(ans, left + right)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans






# Optimal:
class Solution:
    def longestUnivaluePath(self, root):
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_path = 0
            right_path = 0

            if node.left and node.left.val == node.val:
                left_path = left + 1

            if node.right and node.right.val == node.val:
                right_path = right + 1

            ans = max(ans, left_path + right_path)

            return max(left_path, right_path)

        dfs(root)
        return ans