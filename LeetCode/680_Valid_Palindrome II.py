# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.








# Brute force:
class Solution:
    def validPalindrome(self, s):
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        if isPalindrome(0, len(s) - 1):
            return True

        for i in range(len(s)):
            if isPalindrome(0, i - 1) and isPalindrome(i + 1, len(s) - 1):
                return True

        return False









# Optimal:
class Solution:
    def validPalindrome(self, s):
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return (
                    check(left + 1, right) or
                    check(left, right - 1)
                )

            left += 1
            right -= 1

        return True