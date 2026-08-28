# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.







# Brute force:
class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for length in range(1, n):
            if n % length != 0:
                continue

            pattern = s[:length]

            if pattern * (n // length) == s:
                return True

        return False






# Optimal:
class Solution:
    def repeatedSubstringPattern(self, s):
        return s in (s + s)[1:-1]