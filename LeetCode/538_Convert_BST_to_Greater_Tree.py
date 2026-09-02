# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -104 <= Node.val <= 104
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.











# Brute force:
class Solution:
    def convertBST(self, root):
        if not root:
            return root

        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        for i in range(len(nodes)):
            total = 0
            for j in range(i + 1, len(nodes)):
                total += nodes[j].val

            nodes[i].val += total

        return root






# Optimal:
class Solution:
    def convertBST(self, root):
        total = 0

        def reverse_inorder(node):
            nonlocal total

            if not node:
                return

            reverse_inorder(node.right)

            total += node.val
            node.val = total

            reverse_inorder(node.left)

        reverse_inorder(root)

        return root