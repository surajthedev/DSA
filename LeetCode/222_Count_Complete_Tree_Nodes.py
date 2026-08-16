# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.







# Brute force:
class Solution:
    def countNodes(self, root):
        if root is None:
            return 0

        return (
            1
            + self.countNodes(root.left)
            + self.countNodes(root.right)
        )





# Optimal:
class Solution:
    def countNodes(self, root):

        if root is None:
            return 0

        def get_height(node):
            height = 0

            while node:
                height += 1
                node = node.left

            return height

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if left_height == right_height:
            # Left subtree is completely full
            return (2 ** left_height) + self.countNodes(root.right)

        else:
            # Right subtree is completely full
            return (2 ** right_height) + self.countNodes(root.left)