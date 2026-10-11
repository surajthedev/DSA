# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.



# Example 1:


# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:

# Input: root = [0]
# Output: 0


# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.
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
#
#
#
#
# ### Brute Force — DFS

python
```

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, path):
            if not node:
                return 0

            path = path * 2 + node.val

            if not node.left and not node.right:
                return path

            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)
```

### Optimal — DFS (Bit Manipulation)

python
```

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total = 0

        def dfs(node, value):
            nonlocal total

            if not node:
                return

            value = (value << 1) | node.val

            if not node.left and not node.right:
                total += value
                return

            dfs(node.left, value)
            dfs(node.right, value)

        dfs(root, 0)
        return total
```
