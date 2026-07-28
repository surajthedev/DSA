# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.





# Brute Force Approach:
class Solution:
    def isValid(self, t):
        stack = []

        for ch in t:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack.pop()

        return len(stack) == 0

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                if (j - i) % 2 == 0:
                    if self.isValid(s[i:j]):
                        ans = max(ans, j - i)

        return ans







# Optimal Approach:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans