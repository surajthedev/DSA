# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.



# Example 1:


# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Example 2:

# Input: n = 3
# Output: [[0,0,0]]


# Constraints:

# 1 <= n <= 20
#
#
#
#
#
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return []

        def build(nodes):
            if nodes == 1:
                return [TreeNode(0)]

            result = []

            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - 1 - left_nodes

                left_trees = build(left_nodes)
                right_trees = build(right_nodes)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result

        return build(n)














# Optimal:
class Solution:
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return []

        memo = {1: [TreeNode(0)]}

        def build(nodes):
            if nodes in memo:
                return memo[nodes]

            result = []

            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - 1 - left_nodes

                for left in build(left_nodes):
                    for right in build(right_nodes):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            memo[nodes] = result
            return result

        return build(n)
