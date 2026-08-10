# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000




# Brute force:
from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        # Top -> Bottom ko Bottom -> Top karo
        result.reverse()

        return result





# Optimal:
from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = deque([root])
        result = deque()

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Level ko result ke beginning mein add karo
            result.appendleft(level)

        return list(result)