# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



# Example 1:


# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:


# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false


# Constraints:

# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def get_leaves(root):
            if not root:
                return []

            if not root.left and not root.right:
                return [root.val]

            return get_leaves(root.left) + get_leaves(root.right)

        return get_leaves(root1) == get_leaves(root2)








# Optimal:
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(root, leaves):
            if not root:
                return

            if not root.left and not root.right:
                leaves.append(root.val)
                return

            dfs(root.left, leaves)
            dfs(root.right, leaves)

        leaves1 = []
        leaves2 = []

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
