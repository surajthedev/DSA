# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

# Example 1:

# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"
 

# Constraints:

# 1 <= s.length <= 100
# s consists of printable ASCII characters.







# Brute force:
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for ch in s:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch

        return result






# Optimal:
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
