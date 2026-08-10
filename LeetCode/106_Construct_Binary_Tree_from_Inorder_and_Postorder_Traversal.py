# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.



# Brute force:
class Solution:
    def buildTree(self, inorder, postorder):

        if not inorder or not postorder:
            return None

        # Postorder ka last element = root
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Inorder mein root ka index
        root_index = inorder.index(root_val)

        # Left subtree
        left_inorder = inorder[:root_index]
        left_postorder = postorder[:root_index]

        # Right subtree
        right_inorder = inorder[root_index + 1:]
        right_postorder = postorder[root_index:-1]

        root.left = self.buildTree(
            left_inorder,
            left_postorder
        )

        root.right = self.buildTree(
            right_inorder,
            right_postorder
        )

        return root






# Optimal:
class Solution:
    def buildTree(self, inorder, postorder):

        # Inorder ke values ke indexes store karo
        inorder_index = {
            value: i
            for i, value in enumerate(inorder)
        }

        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            # Invalid range
            if left > right:
                return None

            # Postorder ka current last element = root
            root_val = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_val)

            # Inorder mein root ki position
            mid = inorder_index[root_val]

            # IMPORTANT:
            # Postorder right -> left read ho raha hai
            # Isliye pehle RIGHT subtree banana hai.
            root.right = build(mid + 1, right)

            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)