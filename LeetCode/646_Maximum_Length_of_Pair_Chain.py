# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

# Return the length longest chain which can be formed.

# You do not need to use up all the given intervals. You can select pairs in any order.

 

# Example 1:

# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# Example 2:

# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

# Constraints:

# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000









# Brute force:
class Solution:
    def findLongestChain(self, pairs):
        pairs.sort()

        n = len(pairs)
        dp = [1] * n

        ans = 1

        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

            ans = max(ans, dp[i])

        return ans









# Optimal:
class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])

        ans = 0
        prev_end = float("-inf")

        for left, right in pairs:
            if left > prev_end:
                ans += 1
                prev_end = right

        return ans