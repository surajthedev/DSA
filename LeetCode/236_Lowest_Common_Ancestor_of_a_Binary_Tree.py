# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.






# Brute force:
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        def find_path(node, target, path):
            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            if find_path(node.left, target, path):
                return True

            if find_path(node.right, target, path):
                return True

            path.pop()
            return False

        path_p = []
        path_q = []

        find_path(root, p, path_p)
        find_path(root, q, path_q)

        lca = None
        i = 0

        while i < len(path_p) and i < len(path_q):
            if path_p[i] != path_q[i]:
                break

            lca = path_p[i]
            i += 1

        return lca







# Optimal:
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        # Base case
        if root is None:
            return None

        # Current node is one of p or q
        if root == p or root == q:
            return root

        # Search both subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found in different subtrees
        if left and right:
            return root

        # Only one side contains p/q
        return left if left else right