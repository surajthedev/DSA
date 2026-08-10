# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100





# Brute force:
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        levels = []

        # Normal level order traversal
        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            levels.append(level)

        # Zigzag banane ke liye alternate levels reverse
        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i].reverse()

        return levels





# Optimal:
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
            level = deque()

            for _ in range(len(queue)):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(list(level))

            left_to_right = not left_to_right

        return result