# You are given a string s of length n where s[i] is either:

# 'D' means decreasing, or
# 'I' means increasing.
# A permutation perm of n + 1 integers of all the integers in the range [0, n] is called a valid permutation if for all valid i:

# If s[i] == 'D', then perm[i] > perm[i + 1], and
# If s[i] == 'I', then perm[i] < perm[i + 1].
# Return the number of valid permutations perm. Since the answer may be large, return it modulo 109 + 7.



# Example 1:

# Input: s = "DID"
# Output: 5
# Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
# Example 2:

# Input: s = "D"
# Output: 1


# Constraints:

# n == s.length
# 1 <= n <= 200
# s[i] is either 'I' or 'D'.
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
# Brute Force
from itertools import permutations

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        ans = 0

        for perm in permutations(range(n + 1)):
            valid = True

            for i in range(n):
                if s[i] == 'I' and perm[i] >= perm[i + 1]:
                    valid = False
                    break
                if s[i] == 'D' and perm[i] <= perm[i + 1]:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans % (10**9 + 7)


















# Optimal - DP
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            if s[i - 1] == 'I':
                prefix = 0
                for j in range(n - i + 1):
                    prefix = (prefix + dp[i - 1][j]) % MOD
                    dp[i][j] = prefix
            else:
                suffix = 0
                for j in range(n - i, -1, -1):
                    suffix = (suffix + dp[i - 1][j + 1]) % MOD
                    dp[i][j] = suffix

        return dp[n][0] % MOD
