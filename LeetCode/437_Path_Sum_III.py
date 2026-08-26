# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:


# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
 

# Constraints:

# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000





# Brute force:
class Solution:
    def pathSum(self, root, targetSum):

        def count_from(node, remaining):
            if not node:
                return 0

            count = 0

            if node.val == remaining:
                count += 1

            count += count_from(node.left, remaining - node.val)
            count += count_from(node.right, remaining - node.val)

            return count

        if not root:
            return 0

        # Root ko starting point maan kar
        # saare paths count karo
        return (
            count_from(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )






# Optimal:
class Solution:
    def pathSum(self, root, targetSum):

        prefix_count = {0: 1}

        def dfs(node, current_sum):
            if not node:
                return 0

            # Current prefix sum
            current_sum += node.val

            # Required previous prefix
            required = current_sum - targetSum

            # Number of valid paths ending here
            count = prefix_count.get(required, 0)

            # Current prefix ko map mein add karo
            prefix_count[current_sum] = (
                prefix_count.get(current_sum, 0) + 1
            )

            # Left + right
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Backtracking
            prefix_count[current_sum] -= 1

            return count

        return dfs(root, 0)