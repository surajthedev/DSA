# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105









# Brute force:
# Brute Force
class Solution:
    def findTarget(self, root, k):
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if values[i] + values[j] == k:
                    return True

        return False












# Optimal:
# Optimal - Inorder + Two Pointers
class Solution:
    def findTarget(self, root, k):
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        left, right = 0, len(values) - 1

        while left < right:
            total = values[left] + values[right]

            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1

        return False