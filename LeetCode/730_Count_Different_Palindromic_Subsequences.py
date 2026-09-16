# Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

# A subsequence of a string is obtained by deleting zero or more characters from the string.

# A sequence is palindromic if it is equal to the sequence reversed.

# Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

 

# Example 1:

# Input: s = "bccb"
# Output: 6
# Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
# Example 2:

# Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
# Output: 104860361
# Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 109 + 7.
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either 'a', 'b', 'c', or 'd'.












# Brute force:
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        seen = set()

        def dfs(i, curr):
            if curr:
                if curr == curr[::-1]:
                    seen.add(curr)

            for j in range(i, n):
                dfs(j + 1, curr + s[j])

        dfs(0, "")
        return len(seen) % MOD












# Optimal:
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] != s[r]:
                    dp[l][r] = (
                        dp[l + 1][r] +
                        dp[l][r - 1] -
                        dp[l + 1][r - 1]
                    ) % MOD

                else:
                    left = l + 1
                    right = r - 1

                    while left <= right and s[left] != s[l]:
                        left += 1

                    while left <= right and s[right] != s[r]:
                        right -= 1

                    if left > right:
                        dp[l][r] = (
                            2 * dp[l + 1][r - 1] + 2
                        ) % MOD
                    elif left == right:
                        dp[l][r] = (
                            2 * dp[l + 1][r - 1] + 1
                        ) % MOD
                    else:
                        dp[l][r] = (
                            2 * dp[l + 1][r - 1] -
                            dp[left + 1][right - 1]
                        ) % MOD

        return dp[0][n - 1]