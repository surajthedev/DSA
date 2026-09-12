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








# Brute force:
class Solution:
    def checkValidString(self, s):
        def dfs(i, balance):
            if balance < 0:
                return False

            if i == len(s):
                return balance == 0

            if s[i] == '(':
                return dfs(i + 1, balance + 1)

            if s[i] == ')':
                return dfs(i + 1, balance - 1)

            return (
                dfs(i + 1, balance + 1) or
                dfs(i + 1, balance - 1) or
                dfs(i + 1, balance)
            )

        return dfs(0, 0)










# Optimal:
class Solution:
    def checkValidString(self, s):
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0