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
# Brute force:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            balance = 0

            for j in range(i, n):
                if s[j] == '(':
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    break

                if balance == 0:
                    ans = max(ans, j - i + 1)

        return ans














# Optimal:
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
