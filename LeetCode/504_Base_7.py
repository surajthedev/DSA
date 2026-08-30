# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 

# Constraints:

# -107 <= num <= 107






# Brute force:
class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        sign = "-" if num < 0 else ""
        num = abs(num)

        digits = []

        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        return sign + ''.join(digits[::-1])








# Optimal:
class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        sign = "-" if num < 0 else ""
        num = abs(num)

        result = ""

        while num:
            result = str(num % 7) + result
            num //= 7

        return sign + result