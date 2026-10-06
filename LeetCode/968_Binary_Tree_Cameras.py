# You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

# Return the minimum number of cameras needed to monitor all nodes of the tree.



# Example 1:


# Input: root = [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
# Example 2:


# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.


# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# Node.val == 0
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
#
#
# Brute force:
# Brute Force
# Try every possible camera placement.
# Time: O(2^n)
# Space: O(n)

class Solution:
    def minCameraCover(self, root):
        nodes = []

        def collect(node):
            if not node:
                return
            nodes.append(node)
            collect(node.left)
            collect(node.right)

        collect(root)

        n = len(nodes)
        parent = {}

        for node in nodes:
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node

        for mask in range(1 << n):
            cameras = mask.bit_count()

            if cameras >= n:
                continue

            monitored = set()

            for i in range(n):
                if mask & (1 << i):
                    node = nodes[i]
                    monitored.add(node)

                    if node.left:
                        monitored.add(node.left)

                    if node.right:
                        monitored.add(node.right)

                    if node in parent:
                        monitored.add(parent[node])

            if len(monitored) == n:
                return cameras

        return 0












# Optimal - Greedy DFS
# Time: O(n)
# Space: O(h)

class Solution:
    def minCameraCover(self, root):
        cameras = 0

        # 0 = Not covered
        # 1 = Has camera
        # 2 = Covered

        def dfs(node):
            nonlocal cameras

            if not node:
                return 2

            left = dfs(node.left)
            right = dfs(node.right)

            # If any child is not covered,
            # put camera on current node.
            if left == 0 or right == 0:
                cameras += 1
                return 1

            # If any child has camera,
            # current node is covered.
            if left == 1 or right == 1:
                return 2

            # Current node is not covered.
            return 0

        # Root needs special handling.
        if dfs(root) == 0:
            cameras += 1

        return cameras
