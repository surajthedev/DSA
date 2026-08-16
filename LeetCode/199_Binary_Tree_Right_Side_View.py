# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Explanation:



# Example 3:

# Input: root = [1,null,3]

# Output: [1,3]

# Example 4:

# Input: root = []

# Output: []

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100








# Brute force:
class Solution:
    def rightSideView(self, root):
        result = []

        def dfs(node, depth):
            if not node:
                return

            # First node we see at this depth
            if depth == len(result):
                result.append(node.val)

            # Right first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return result





# Optimal:
class Solution:
    def rightSideView(self, root):
        result = []

        def dfs(node, depth):
            if not node:
                return

            # Is depth ka pehla node = rightmost node
            if depth == len(result):
                result.append(node.val)

            # Right ko pehle visit karo
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return result