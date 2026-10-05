# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
# Example 2:


# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.


# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
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
# Brute force:
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        levels = []
        queue = [root]

        while queue:
            next_queue = []
            level = []

            for node in queue:
                if node:
                    level.append(node)
                    next_queue.append(node.left)
                    next_queue.append(node.right)

            if not level:
                break

            levels.append(level)
            queue = next_queue

        for i in range(len(levels) - 1):
            if len(levels[i]) != 2 ** i:
                return False

        last = levels[-1]

        return len(last) <= 2 ** (len(levels) - 1)












# Optimal:
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        seen_null = False

        while queue:
            node = queue.pop(0)

            if node is None:
                seen_null = True
                continue

            if seen_null:
                return False

            queue.append(node.left)
            queue.append(node.right)

        return True
