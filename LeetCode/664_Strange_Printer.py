# There is a strange printer with the following two special properties:

# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.

 

# Example 1:

# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters.








# Brute force:
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        memo = {}

        def solve(l, r):
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            ans = 1 + solve(l + 1, r)

            for k in range(l + 1, r + 1):
                if s[k] == s[l]:
                    ans = min(
                        ans,
                        solve(l + 1, k - 1) + solve(k, r)
                    )

            memo[(l, r)] = ans
            return ans

        return solve(0, n - 1)








# Optimal:
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                dp[l][r] = dp[l + 1][r] + 1

                for k in range(l + 1, r + 1):
                    if s[k] == s[l]:
                        left = dp[l + 1][k - 1] if k > l + 1 else 0
                        dp[l][r] = min(
                            dp[l][r],
                            left + dp[k][r]
                        )

        return dp[0][n - 1]