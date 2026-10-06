# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.



# Example 1:


# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:


# Input: root = [2,2,2,5,2]
# Output: false


# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100
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
# # Brute Force - O(n) Time, O(n) Space

class Solution:
    def isUnivalTree(self, root):
        values = []

        def dfs(node):
            if not node:
                return

            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return len(set(values)) == 1


# Optimal - O(n) Time, O(h) Space

class Solution:
    def isUnivalTree(self, root):
        value = root.val

        def dfs(node):
            if not node:
                return True

            if node.val != value:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)
