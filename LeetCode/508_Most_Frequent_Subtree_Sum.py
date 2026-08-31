# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

 

# Example 1:


# Input: root = [5,2,-3]
# Output: [2,-3,4]
# Example 2:


# Input: root = [5,2,-5]
# Output: [2]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105







# Brute force:
class Solution:
    def findFrequentTreeSum(self, root):
        def subtree_sum(node):
            if not node:
                return 0

            return (
                node.val
                + subtree_sum(node.left)
                + subtree_sum(node.right)
            )

        sums = []

        def collect(node):
            if not node:
                return

            sums.append(subtree_sum(node))
            collect(node.left)
            collect(node.right)

        collect(root)

        freq = {}

        for s in sums:
            freq[s] = freq.get(s, 0) + 1

        max_freq = max(freq.values())

        return [s for s in freq if freq[s] == max_freq]








# Optimal:
class Solution:
    def findFrequentTreeSum(self, root):
        from collections import defaultdict

        freq = defaultdict(int)
        max_freq = 0

        def dfs(node):
            nonlocal max_freq

            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)

            freq[total] += 1
            max_freq = max(max_freq, freq[total])

            return total

        dfs(root)

        return [s for s in freq if freq[s] == max_freq]