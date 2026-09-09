# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Example 2:


# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1









# Brute force:
class Solution:
    def averageOfLevels(self, root):
        ans = []
        
        def dfs(node, level):
            if not node:
                return

            if level == len(ans):
                ans.append([0, 0])

            ans[level][0] += node.val
            ans[level][1] += 1

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return [total / count for total, count in ans]










# Optimal:
from collections import deque

class Solution:
    def averageOfLevels(self, root):
        ans = []
        q = deque([root])

        while q:
            level_sum = 0
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level_sum / level_size)

        return ans