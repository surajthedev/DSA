# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.



# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Example 2:

# Input: root = [1], target = 1, k = 3
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def distanceK(self, root, target, k):
        parent = {}

        def build(node, par=None):
            if not node:
                return

            parent[node] = par
            build(node.left, node)
            build(node.right, node)

        build(root)

        target_node = None

        def find(node):
            nonlocal target_node

            if not node:
                return

            if node.val == target:
                target_node = node
                return

            find(node.left)
            find(node.right)

        find(root)

        def dfs(node, distance, visited):
            if not node or node in visited:
                return []

            visited.add(node)

            if distance == k:
                return [node.val]

            result = []
            result += dfs(node.left, distance + 1, visited)
            result += dfs(node.right, distance + 1, visited)
            result += dfs(parent[node], distance + 1, visited)

            return result

        return dfs(target_node, 0, set())










# Optimal:
from collections import deque

class Solution:
    def distanceK(self, root, target, k):
        parent = {}

        def dfs(node, par=None):
            if not node:
                return

            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        queue = deque([target])
        visited = {target}
        distance = 0

        while queue:
            if distance == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                if parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])

            distance += 1

        return []
