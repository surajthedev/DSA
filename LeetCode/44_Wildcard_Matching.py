# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

# Constraints:

# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.


# Brute Force:
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def solve(i, j):

            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if i == len(s):
                while j < len(p):
                    if p[j] != '*':
                        return False
                    j += 1
                return True

            if s[i] == p[j] or p[j] == '?':
                return solve(i + 1, j + 1)

            if p[j] == '*':
                return solve(i, j + 1) or solve(i + 1, j)

            return False

        return solve(0, 0)




# Optimized DP
class Solution:
    def isMatch(self, s: str, p: str):

        n = len(s)
        m = len(p)

        prev = [False] * (m + 1)
        prev[0] = True

        for j in range(1, m + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]

        for i in range(1, n + 1):

            curr = [False] * (m + 1)

            for j in range(1, m + 1):

                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    curr[j] = prev[j - 1]

                elif p[j - 1] == '*':
                    curr[j] = curr[j - 1] or prev[j]

            prev = curr

        return prev[m]