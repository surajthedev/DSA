# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true
# Example 3:

# Input: s = "(*))"
# Output: true
# Example 4:

# Input: s = "("
# Output: false


# Constraints:

# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.
#
#
#
#
#
#
#
#
#
#
#
# Brute Force
class Solution:
    def checkValidString(self, s: str) -> bool:
        def solve(i, balance):
            if balance < 0:
                return False

            if i == len(s):
                return balance == 0

            if s[i] == '(':
                return solve(i + 1, balance + 1)
            elif s[i] == ')':
                return solve(i + 1, balance - 1)
            else:
                return (
                    solve(i + 1, balance + 1) or
                    solve(i + 1, balance - 1) or
                    solve(i + 1, balance)
                )

        return solve(0, 0)













# Optimal - Greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low = max(0, low - 1)
                high -= 1
            else:
                low = max(0, low - 1)
                high += 1

            if high < 0:
                return False

        return low == 0
