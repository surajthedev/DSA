# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.


# Example 1:

# Input: s = "()"
# Output: 1
# Example 2:

# Input: s = "(())"
# Output: 2
# Example 3:

# Input: s = "()()"
# Output: 2


# Constraints:

# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.
#
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def solve(s):
            if s == "()":
                return 1

            balance = 0
            parts = []
            start = 0

            for i, ch in enumerate(s):
                balance += 1 if ch == '(' else -1

                if balance == 0:
                    parts.append(s[start:i + 1])
                    start = i + 1

            ans = 0

            for part in parts:
                if part == "()":
                    ans += 1
                else:
                    ans += 2 * solve(part[1:-1])

            return ans

        return solve(s)










# Optimal:
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inner = stack.pop()
                stack[-1] += max(2 * inner, 1)

        return stack[0]
