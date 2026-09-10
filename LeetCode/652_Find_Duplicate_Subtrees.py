# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

 

# Example 1:


# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:


# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:


# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
 

# Constraints:

# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200








# BRute force:
# Brute Force
class Solution:
    def findDuplicateSubtrees(self, root):
        result = []
        seen = {}

        def serialize(node):
            if not node:
                return "#"

            s = f"{node.val},{serialize(node.left)},{serialize(node.right)}"

            if s in seen:
                if seen[s] == 1:
                    result.append(node)
                seen[s] += 1
            else:
                seen[s] = 1

            return s

        serialize(root)
        return result












# Optimal:
# Optimal - Unique ID / Hashing
class Solution:
    def findDuplicateSubtrees(self, root):
        result = []
        count = {}
        ids = {}
        next_id = 1

        def dfs(node):
            nonlocal next_id

            if not node:
                return 0

            left_id = dfs(node.left)
            right_id = dfs(node.right)

            key = (node.val, left_id, right_id)

            if key not in ids:
                ids[key] = next_id
                next_id += 1

            tree_id = ids[key]

            count[tree_id] = count.get(tree_id, 0) + 1

            if count[tree_id] == 2:
                result.append(node)

            return tree_id

        dfs(root)
        return result