# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

# Example 1:


# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:


# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 104





# Brute force:
class Solution:
    def rob(self, root):

        if not root:
            return 0

        # Rob current node
        rob_current = root.val

        if root.left:
            rob_current += self.rob(root.left.left)
            rob_current += self.rob(root.left.right)

        if root.right:
            rob_current += self.rob(root.right.left)
            rob_current += self.rob(root.right.right)

        # Skip current node
        skip_current = (
            self.rob(root.left) +
            self.rob(root.right)
        )

        return max(rob_current, skip_current)






# Optimal:
class Solution:
    def rob(self, root):

        def dfs(node):
            if not node:
                return (0, 0)

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # Rob current node
            rob = node.val + left_skip + right_skip

            # Skip current node
            skip = (
                max(left_rob, left_skip) +
                max(right_rob, right_skip)
            )

            return (rob, skip)

        rob, skip = dfs(root)

        return max(rob, skip)