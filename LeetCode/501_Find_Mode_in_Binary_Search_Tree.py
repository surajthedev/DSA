# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105







# Brute force:
class Solution:
    def findMode(self, root):
        from collections import Counter

        freq = Counter()

        def dfs(node):
            if not node:
                return

            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_freq = max(freq.values())

        return [key for key, value in freq.items() if value == max_freq]








# Optimal:
class Solution:
    def findMode(self, root):
        ans = []
        max_count = 0
        count = 0
        prev = None

        def inorder(node):
            nonlocal count, max_count, prev

            if not node:
                return

            inorder(node.left)

            if prev == node.val:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                ans.clear()
                ans.append(node.val)
            elif count == max_count:
                ans.append(node.val)

            prev = node.val

            inorder(node.right)

        inorder(root)

        return ans