# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105






# Brute force:
class Solution:
    def getMinimumDifference(self, root):
        values = []

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        ans = float('inf')

        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                ans = min(ans, abs(values[i] - values[j]))

        return ans







# Optimal:
class Solution:
    def getMinimumDifference(self, root):
        prev = None
        ans = float('inf')

        def inorder(node):
            nonlocal prev, ans

            if not node:
                return

            inorder(node.left)

            if prev is not None:
                ans = min(ans, node.val - prev)

            prev = node.val

            inorder(node.right)

        inorder(root)

        return ans