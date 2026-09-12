# You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

# You are restricted with the following rules:

# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.

 

# Example 1:

# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24
# Example 2:

# Input: cards = [1,2,1,2]
# Output: false
 

# Constraints:

# cards.length == 4
# 1 <= cards[i] <= 9










# Brute force:
from itertools import permutations, product

class Solution:
    def judgePoint24(self, cards):
        def calc(a, b, op):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if b != 0:
                return a / b
            return None

        for nums in permutations(cards):
            for ops in product("+-*/", repeat=3):
                a, b, c, d = nums
                op1, op2, op3 = ops

                # ((a op1 b) op2 c) op3 d
                x = calc(a, b, op1)
                if x is not None:
                    x = calc(x, c, op2)
                    if x is not None:
                        x = calc(x, d, op3)
                        if x is not None and abs(x - 24) < 1e-6:
                            return True

                # (a op1 (b op2 c)) op3 d
                x = calc(b, c, op2)
                if x is not None:
                    x = calc(a, x, op1)
                    if x is not None:
                        x = calc(x, d, op3)
                        if x is not None and abs(x - 24) < 1e-6:
                            return True

                # a op1 ((b op2 c) op3 d)
                x = calc(b, c, op2)
                if x is not None:
                    x = calc(x, d, op3)
                    if x is not None:
                        x = calc(a, x, op1)
                        if x is not None and abs(x - 24) < 1e-6:
                            return True

                # a op1 (b op2 (c op3 d))
                x = calc(c, d, op3)
                if x is not None:
                    x = calc(b, x, op2)
                    if x is not None:
                        x = calc(a, x, op1)
                        if x is not None and abs(x - 24) < 1e-6:
                            return True

                # (a op1 b) op2 (c op3 d)
                x = calc(a, b, op1)
                y = calc(c, d, op3)
                if x is not None and y is not None:
                    x = calc(x, y, op2)
                    if x is not None and abs(x - 24) < 1e-6:
                        return True

        return False









# Optimal:
class Solution:
    def judgePoint24(self, cards):
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            n = len(nums)

            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]

                    rest = [
                        nums[k]
                        for k in range(n)
                        if k != i and k != j
                    ]

                    results = [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]

                    if abs(b) > 1e-9:
                        results.append(a / b)

                    if abs(a) > 1e-9:
                        results.append(b / a)

                    for value in results:
                        if dfs(rest + [value]):
                            return True

            return False

        return dfs([float(x) for x in cards])