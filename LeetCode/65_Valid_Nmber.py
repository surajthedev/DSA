# Given a string s, return whether s is a valid number.

# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

# Formally, a valid number is defined using one of the following definitions:

# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.

# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

# The digits are defined as one or more digits.

 

# Example 1:

# Input: s = "0"

# Output: true

# Example 2:

# Input: s = "e"

# Output: false

# Example 3:

# Input: s = "."

# Output: false

 

# Constraints:

# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.


# Brute Force:
import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$'
        return re.fullmatch(pattern, s) is not None




# Optimal:
class Solution:
    def isNumber(self, s: str) -> bool:

        seenDigit = False
        seenDot = False
        seenExponent = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                seenDigit = True

            elif ch in ['+', '-']:
                # Sign should be at beginning or just after e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            elif ch == '.':
                # Dot cannot appear after exponent or twice
                if seenDot or seenExponent:
                    return False
                seenDot = True

            elif ch in ['e', 'E']:
                # Exponent cannot repeat and must follow a digit
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False   # Need digits after exponent

            else:
                return False

        return seenDigit