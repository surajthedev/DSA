# You are given a string s and a positive integer k.

# Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

# The length of each substring is at least k.
# Each substring is a palindrome.
# Return the maximum number of substrings in an optimal selection.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "abaccdbbd", k = 3
# Output: 2
# Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
# It can be shown that we cannot find a selection with more than two valid substrings.
# Example 2:

# Input: s = "adbcda", k = 2
# Output: 0
# Explanation: There is no palindrome substring of length at least 2 in the string.
 

# Constraints:

# 1 <= k <= s.length <= 2000
# s consists of lowercase English letters.






# Brute Force
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        intervals = []

        for i in range(n):
            for j in range(i + k - 1, n):
                if is_palindrome(i, j):
                    intervals.append((i, j))

        intervals.sort(key=lambda x: x[1])

        ans = 0
        end = -1

        for l, r in intervals:
            if l > end:
                ans += 1
                end = r

        return ans







# Optimal
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        dp = [0] * (n + 1)

        # pal[l] = whether s[l..r] is palindrome for current r
        pal = [False] * n

        for r in range(n):
            prev = False

            for l in range(r, -1, -1):
                cur = s[l] == s[r] and (r - l < 2 or prev)
                prev = pal[l]
                pal[l] = cur

                if cur and r - l + 1 >= k:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

            dp[r + 1] = max(dp[r + 1], dp[r])

        return dp[n]
