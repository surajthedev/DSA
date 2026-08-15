# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
 

# Constraints:

# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].






# Brute force:
class Solution:
    def titleToNumber(self, columnTitle):
        current = "A"
        number = 1

        while current != columnTitle:
            number += 1

            # Convert number to Excel title
            n = number
            temp = []

            while n > 0:
                n -= 1
                remainder = n % 26
                temp.append(chr(ord('A') + remainder))
                n //= 26

            current = ''.join(reversed(temp))

        return number









# Optimal:
class Solution:
    def titleToNumber(self, columnTitle):
        result = 0

        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            result = result * 26 + value

        return result