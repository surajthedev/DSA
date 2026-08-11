# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000








# Brute force:
class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path):
            if node is None:
                return

            path.append(node.val)

            # Leaf node
            if node.left is None and node.right is None:
                if sum(path) == targetSum:
                    result.append(path.copy())

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        dfs(root, [])

        return result




# Optimal:
class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if node is None:
                return

            # Add current node
            path.append(node.val)
            remaining -= node.val

            # Leaf node
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path.copy())

            # Explore left and right
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])

        return result