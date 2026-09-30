# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

# If there exist multiple answers, you can return any of them.



# Example 1:


# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# Example 2:

# Input: preorder = [1], postorder = [1]
# Output: [1]


# Constraints:

# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
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
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        left_root = preorder[1]
        left_size = postorder.index(left_root) + 1

        root.left = self.constructFromPrePost(
            preorder[1:left_size + 1],
            postorder[:left_size]
        )

        root.right = self.constructFromPrePost(
            preorder[left_size + 1:],
            postorder[left_size:-1]
        )

        return root














# Optimal:
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        post_index = {val: i for i, val in enumerate(postorder)}

        def build(pre_l, pre_r, post_l, post_r):
            if pre_l > pre_r:
                return None

            root = TreeNode(preorder[pre_l])

            if pre_l == pre_r:
                return root

            left_root = preorder[pre_l + 1]
            left_size = post_index[left_root] - post_l + 1

            root.left = build(
                pre_l + 1,
                pre_l + left_size,
                post_l,
                post_l + left_size - 1
            )

            root.right = build(
                pre_l + left_size + 1,
                pre_r,
                post_l + left_size,
                post_r - 1
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
