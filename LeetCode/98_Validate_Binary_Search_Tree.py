# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1



# Brute force:
class Solution:
    def isValidBST(self, root):
        if root is None:
            return True

        # Check all values in left subtree
        if not self.checkLess(root.left, root.val):
            return False

        # Check all values in right subtree
        if not self.checkGreater(root.right, root.val):
            return False

        # Recursively check both subtrees
        return (
            self.isValidBST(root.left)
            and self.isValidBST(root.right)
        )

    def checkLess(self, root, value):
        if root is None:
            return True

        if root.val >= value:
            return False

        return (
            self.checkLess(root.left, value)
            and self.checkLess(root.right, value)
        )

    def checkGreater(self, root, value):
        if root is None:
            return True

        if root.val <= value:
            return False

        return (
            self.checkGreater(root.left, value)
            and self.checkGreater(root.right, value)
        )





# Optimal:
class Solution:
    def isValidBST(self, root):
        def dfs(node, low, high):
            if node is None:
                return True

            # Node must be strictly inside the range
            if node.val <= low or node.val >= high:
                return False

            # Left subtree: values must be < node.val
            # Right subtree: values must be > node.val
            return (
                dfs(node.left, low, node.val)
                and
                dfs(node.right, node.val, high)
            )

        return dfs(root, float("-inf"), float("inf"))