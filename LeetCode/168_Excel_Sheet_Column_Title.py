# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
 

# Constraints:

# 1 <= columnNumber <= 231 - 1







# Brute force:
class Solution:
    def convertToTitle(self, columnNumber):
        result = ""

        for num in range(1, columnNumber + 1):
            temp = ""
            n = num

            while n > 0:
                n -= 1
                remainder = n % 26
                temp = chr(ord('A') + remainder) + temp
                n //= 26

            result = temp

        return result










# Optimal:
class Solution:
    def convertToTitle(self, columnNumber):
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26

            result.append(chr(ord('A') + remainder))

            columnNumber //= 26

        return ''.join(reversed(result))