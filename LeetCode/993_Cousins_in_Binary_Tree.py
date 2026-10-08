# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.



# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:


# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false


# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.
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
# ## Brute Force — DFS

```
class Solution:
    def isCousins(self, root, x, y):
        def dfs(node, parent, depth, target):
            if not node:
                return None

            if node.val == target:
                return (parent, depth)

            left = dfs(node.left, node, depth + 1, target)
            if left:
                return left

            return dfs(node.right, node, depth + 1, target)

        parent_x, depth_x = dfs(root, None, 0, x)
        parent_y, depth_y = dfs(root, None, 0, y)

        return depth_x == depth_y and parent_x != parent_y
```

## Optimal — BFS

```
from collections import deque

class Solution:
    def isCousins(self, root, x, y):
        queue = deque([(root, None)])

        while queue:
            size = len(queue)
            parents = {}

            for _ in range(size):
                node, parent = queue.popleft()

                if node.val == x:
                    parents[x] = parent

                if node.val == y:
                    parents[y] = parent

                if node.left:
                    queue.append((node.left, node))

                if node.right:
                    queue.append((node.right, node))

            if x in parents or y in parents:
                return x in parents and y in parents and parents[x] != parents[y]

        return False
```
