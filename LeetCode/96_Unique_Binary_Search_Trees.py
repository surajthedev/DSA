# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

# Example 1:


# Input: n = 3
# Output: 5
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 19


# Brute force:
class Solution:
    def numTrees(self, n):

        def count(nodes):
            # Empty tree
            if nodes <= 1:
                return 1

            total = 0

            # Har possible root
            for left_nodes in range(nodes):

                right_nodes = nodes - 1 - left_nodes

                left_count = count(left_nodes)
                right_count = count(right_nodes)

                total += left_count * right_count

            return total

        return count(n)







# Optimal:
class Solution:
    def numTrees(self, n):

        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1
        dp[1] = 1

        # Number of nodes
        for nodes in range(2, n + 1):

            # Har possible root
            for left_nodes in range(nodes):

                right_nodes = nodes - 1 - left_nodes

                dp[nodes] += dp[left_nodes] * dp[right_nodes]

        return dp[n]