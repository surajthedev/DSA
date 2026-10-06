# You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

# Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:


# Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

# Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].



# Example 1:


# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
# Example 2:


# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.
# Example 3:


# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.


# Constraints:

# The number of nodes in the tree is n.
# n == voyage.length
# 1 <= n <= 100
# 1 <= Node.val, voyage[i] <= n
# All the values in the tree are unique.
# All the values in voyage are unique.
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
# # Brute Force
# Try all possible flip combinations.
# Time: O(2^n * n)
# Space: O(n)

class Solution:
    def flipMatchVoyage(self, root, voyage):
        ans = []
        n = len(voyage)

        def preorder(node, flips):
            if not node:
                return []

            if node.left:
                left = preorder(node.left, flips)
            else:
                left = []

            if node.right:
                right = preorder(node.right, flips)
            else:
                right = []

            if node.left and node.right and left + right != voyage[:len(left) + len(right) + 1]:
                flips.append(node.val)

            return [node.val] + left + right

        # Generate all flip combinations
        nodes = []

        def collect(node):
            if not node:
                return
            nodes.append(node)
            collect(node.left)
            collect(node.right)

        collect(root)

        for mask in range(1 << len(nodes)):
            def dfs(node):
                if not node:
                    return []

                if mask & (1 << nodes.index(node)):
                    return [node.val] + dfs(node.right) + dfs(node.left)

                return [node.val] + dfs(node.left) + dfs(node.right)

            if dfs(root) == voyage:
                return [
                    nodes[i].val
                    for i in range(len(nodes))
                    if mask & (1 << i)
                ]

        return [-1]














# Optimal - Greedy DFS
# Time: O(n)
# Space: O(n)

class Solution:
    def flipMatchVoyage(self, root, voyage):
        ans = []
        index = 0

        def dfs(node):
            nonlocal index

            if not node:
                return True

            # Current node must match voyage
            if index >= len(voyage) or node.val != voyage[index]:
                return False

            index += 1

            # Flip if left child doesn't match next voyage value
            if node.left and index < len(voyage) and node.left.val != voyage[index]:
                if not node.right:
                    return False

                ans.append(node.val)

                if not dfs(node.right):
                    return False

                if not dfs(node.left):
                    return False

            else:
                if not dfs(node.left):
                    return False

                if not dfs(node.right):
                    return False

            return True

        if dfs(root):
            return ans

        return [-1]
