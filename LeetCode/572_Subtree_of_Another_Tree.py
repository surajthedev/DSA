# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104








# Brute force:
class Solution:
    def isSubtree(self, root, subRoot):
        def same(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False

            return (
                a.val == b.val
                and same(a.left, b.left)
                and same(a.right, b.right)
            )

        def dfs(node):
            if not node:
                return False

            if same(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)






# Optimal:
class Solution:
    def isSubtree(self, root, subRoot):
        def serialize(node):
            if not node:
                return "#"

            return (
                "," + str(node.val)
                + serialize(node.left)
                + serialize(node.right)
            )

        root_str = serialize(root)
        sub_str = serialize(subRoot)

        return sub_str in root_str