# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

# Example 1:


# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 8



# Brute force:
class Solution:
    def generateTrees(self, n):
        
        def generate(start, end):
            result = []

            # Empty tree
            if start > end:
                return [None]

            # Har value ko root try karo
            for root_val in range(start, end + 1):

                # Left subtree ke saare possibilities
                left_trees = generate(start, root_val - 1)

                # Right subtree ke saare possibilities
                right_trees = generate(root_val + 1, end)

                # Har left + right combination
                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right

                        result.append(root)

            return result

        return generate(1, n)






# Optimal:
class Solution:
    def generateTrees(self, n):

        memo = {}

        def generate(start, end):

            # Empty tree
            if start > end:
                return [None]

            # Already calculated
            if (start, end) in memo:
                return memo[(start, end)]

            result = []

            # Har value ko root try karo
            for root_val in range(start, end + 1):

                # Left subtree
                left_trees = generate(start, root_val - 1)

                # Right subtree
                right_trees = generate(root_val + 1, end)

                # Left + Right combinations
                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right

                        result.append(root)

            memo[(start, end)] = result

            return result

        return generate(1, n)