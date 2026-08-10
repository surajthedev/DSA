# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.




# Brute force:
class Solution:
    def buildTree(self, preorder, inorder):

        if not preorder or not inorder:
            return None

        # Preorder ka first element = root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Inorder mein root ki position find karo
        root_index = inorder.index(root_val)

        # Left subtree
        left_inorder = inorder[:root_index]
        left_preorder = preorder[1:1 + root_index]

        # Right subtree
        right_inorder = inorder[root_index + 1:]
        right_preorder = preorder[1 + root_index:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root








# Optimal:
class Solution:
    def buildTree(self, preorder, inorder):

        # Inorder mein har value ka index store karo
        inorder_index = {
            value: i
            for i, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            # Invalid range
            if left > right:
                return None

            # Preorder ka current element root hai
            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            # Inorder mein root ki position
            mid = inorder_index[root_val]

            # Left subtree
            root.left = build(left, mid - 1)

            # Right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)