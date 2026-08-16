# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.






# Brute force:
class Solution:
    def calculate(self, s):
        tokens = []
        num = 0

        # Convert string into numbers/operators
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch != ' ':
                tokens.append(num)
                tokens.append(ch)
                num = 0

        tokens.append(num)

        # First pass: * and /
        i = 1

        while i < len(tokens) - 1:
            if tokens[i] == '*' or tokens[i] == '/':
                left = tokens[i - 1]
                right = tokens[i + 1]

                if tokens[i] == '*':
                    value = left * right
                else:
                    # truncate toward zero
                    value = int(left / right)

                tokens[i - 1:i + 2] = [value]
                i = 1
            else:
                i += 2

        # Second pass: + and -
        result = tokens[0]
        i = 1

        while i < len(tokens):
            op = tokens[i]
            num = tokens[i + 1]

            if op == '+':
                result += num
            else:
                result -= num

            i += 2

        return result










# Optimal:
class Solution:
    def calculate(self, s):
        stack = []

        num = 0
        sign = '+'

        for i in range(len(s)):

            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack[-1] = stack[-1] * num

                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)

                sign = ch
                num = 0

        return sum(stack)