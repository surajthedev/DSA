# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100



# Brute force:
class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return

            # Left
            inorder(node.left)

            # Root
            result.append(node.val)

            # Right
            inorder(node.right)

        inorder(root)

        return result





# Optimal:
class Solution:
    def inorderTraversal(self, root):
        result = []
        curr = root

        while curr:

            # Agar left child nahi hai
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right

            else:
                # Inorder predecessor find karo
                predecessor = curr.left

                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                # First time predecessor mil raha hai
                if predecessor.right is None:

                    # Temporary thread banao
                    predecessor.right = curr

                    # Left subtree mein jao
                    curr = curr.left

                else:
                    # Left subtree complete ho gaya
                    # Temporary thread remove karo
                    predecessor.right = None

                    # Current node process karo
                    result.append(curr.val)

                    # Right subtree
                    curr = curr.right

        return result