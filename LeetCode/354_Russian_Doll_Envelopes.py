# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

 

# Example 1:

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:

# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
 

# Constraints:

# 1 <= envelopes.length <= 105
# envelopes[i].length == 2
# 1 <= wi, hi <= 105






# Brute force:
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort()

        n = len(envelopes)
        dp = [1] * n

        ans = 1

        for i in range(n):
            for j in range(i):
                if (envelopes[j][0] < envelopes[i][0] and
                    envelopes[j][1] < envelopes[i][1]):

                    dp[i] = max(dp[i], dp[j] + 1)

            ans = max(ans, dp[i])

        return ans








# Optimal:
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        # Width ascending
        # Same width -> height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        lis = []

        for w, h in envelopes:
            pos = bisect_left(lis, h)

            if pos == len(lis):
                lis.append(h)
            else:
                lis[pos] = h

        return len(lis)