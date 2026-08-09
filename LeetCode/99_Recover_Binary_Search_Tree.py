# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

# Example 1:


# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:


# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

# Constraints:

# The number of nodes in the tree is in the range [2, 1000].
# -231 <= Node.val <= 231 - 1



# Brute force:
class Solution:
    def recoverTree(self, root):
        values = []

        # Step 1: Inorder traversal
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Find correct sorted values
        sorted_values = sorted(values)

        # Step 3: Find the two wrong values
        wrong_values = []

        for i in range(len(values)):
            if values[i] != sorted_values[i]:
                wrong_values.append(values[i])

        first = wrong_values[0]
        second = wrong_values[1]

        # Step 4: Swap the two values in the tree
        def fix(node):
            if not node:
                return

            if node.val == first:
                node.val = second

            elif node.val == second:
                node.val = first

            fix(node.left)
            fix(node.right)

        fix(root)




# Optimal:
class Solution:
    def recoverTree(self, root):
        first = None
        second = None
        prev = None

        def inorder(node):
            nonlocal first, second, prev

            if not node:
                return

            # Left
            inorder(node.left)

            # Current
            if prev and prev.val > node.val:

                # First wrong node
                if first is None:
                    first = prev

                # Second wrong node
                second = node

            prev = node

            # Right
            inorder(node.right)

        inorder(root)

        # Swap the values
        first.val, second.val = second.val, first.val