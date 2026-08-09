# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# Brute force:
class Solution:
    def isSameTree(self, p, q):
        def serialize(root):
            if root is None:
                return [None]

            return [
                root.val,
                *serialize(root.left),
                *serialize(root.right)
            ]

        return serialize(p) == serialize(q)




# Optimal:
class Solution:
    def isSameTree(self, p, q):
        # Both are empty
        if not p and not q:
            return True

        # One is empty, other is not
        if not p or not q:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Compare left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )