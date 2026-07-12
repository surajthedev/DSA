# Given a string s, return the longest palindromic substring in s.
# 
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Brute Force Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(substring):
            return substring == substring[::-1]
            
        longest = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if is_palindrome(sub) and len(sub) > len(longest):
                    longest = sub
                    
        return longest

# Optimal Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            
        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd_pal = expand_around_center(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal
                
            # Even length palindrome
            even_pal = expand_around_center(i, i + 1)
            if len(even_pal) > len(longest):
                longest = even_pal
                
        return longest
