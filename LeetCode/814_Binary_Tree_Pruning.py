# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# A subtree of a node node is node plus every node that is a descendant of node.



# Example 1:


# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# Example 2:


# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# Example 3:


# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]


# Constraints:

# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.
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
#
# Brute force:
class Solution:
    def pruneTree(self, root):
        def contains_one(node):
            if not node:
                return False

            return (
                node.val == 1
                or contains_one(node.left)
                or contains_one(node.right)
            )

        def prune(node):
            if not node:
                return None

            if not contains_one(node):
                return None

            node.left = prune(node.left)
            node.right = prune(node.right)

            return node

        return prune(root)










# Optimal:
class Solution:
    def pruneTree(self, root):
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val == 1 or node.left or node.right:
                return node

            return None

        return dfs(root)
