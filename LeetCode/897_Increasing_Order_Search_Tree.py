# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



# Example 1:


# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:


# Input: root = [5,1,7]
# Output: [1,null,5,null,7]


# Constraints:

# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000
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
    def increasingBST(self, root):
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        dummy = TreeNode(0)
        curr = dummy

        for val in values:
            curr.right = TreeNode(val)
            curr = curr.right

        return dummy.right














# Optimal:
class Solution:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        curr = dummy

        def inorder(node):
            nonlocal curr

            if not node:
                return

            inorder(node.left)

            node.left = None
            curr.right = node
            curr = node

            inorder(node.right)

        inorder(root)

        return dummy.right
