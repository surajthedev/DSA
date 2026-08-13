# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Example 2:

# Input: s = "a"
# Output: 0
# Example 3:

# Input: s = "ab"
# Output: 1
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase English letters only.
 


# Brute force:
class Solution:
    def minCut(self, s):
        n = len(s)

        memo = {}

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def solve(start):
            # Already at the end
            if start == n:
                return -1

            if start in memo:
                return memo[start]

            ans = float('inf')

            for end in range(start, n):
                if isPalindrome(start, end):
                    # One cut after s[start:end+1]
                    cuts = 1 + solve(end + 1)

                    ans = min(ans, cuts)

            memo[start] = ans
            return ans

        return solve(0)







# Optimal:
class Solution:
    def minCut(self, s):
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = minimum cuts needed for s[0:i]
        dp = [float('inf')] * (n + 1)

        dp[0] = -1

        for end in range(n):
            for start in range(end + 1):
                if pal[start][end]:
                    dp[end + 1] = min(
                        dp[end + 1],
                        dp[start] + 1
                    )

        return dp[n]