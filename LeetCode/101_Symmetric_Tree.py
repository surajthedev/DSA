# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100



# Brute force:
class Solution:
    def isSymmetric(self, root):
        left = []
        right = []

        def left_traversal(node):
            if node is None:
                left.append(None)
                return

            left.append(node.val)
            left_traversal(node.left)
            left_traversal(node.right)

        def right_traversal(node):
            if node is None:
                right.append(None)
                return

            right.append(node.val)
            right_traversal(node.right)
            right_traversal(node.left)

        left_traversal(root.left)
        right_traversal(root.right)

        return left == right






# Optimal:
class Solution:
    def isSymmetric(self, root):
        
        def isMirror(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return (
                isMirror(left.left, right.right)
                and
                isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)