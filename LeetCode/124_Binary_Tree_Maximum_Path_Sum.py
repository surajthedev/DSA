# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000




# Optimal:
class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            # Left and right subtree ka maximum gain
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # Current node ko turning point maan kar
            # complete path
            current_path = (
                node.val
                + left_gain
                + right_gain
            )

            # Global answer update
            self.ans = max(self.ans, current_path)

            # Parent ko sirf ek side ka gain de sakte hain
            return node.val + max(left_gain, right_gain)

        dfs(root)

        return self.ans