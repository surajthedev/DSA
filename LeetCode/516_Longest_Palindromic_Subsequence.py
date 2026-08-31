# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.








# Brute force:
class Solution:
    def longestPalindromeSubseq(self, s):
        def dfs(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + dfs(i + 1, j - 1)

            return max(
                dfs(i + 1, j),
                dfs(i, j - 1)
            )

        return dfs(0, len(s) - 1)






# Optimal:
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]