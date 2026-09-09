# Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

 

# Example 1:

# Input: equation = "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:

# Input: equation = "x=x"
# Output: "Infinite solutions"
# Example 3:

# Input: equation = "2x=x"
# Output: "x=0"
 

# Constraints:

# 3 <= equation.length <= 1000
# equation has exactly one '='.
# equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.
# The input is generated that if there is a single solution, it will be an integer.
 








# Solution:
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            coef = 0
            const = 0
            i = 0
            sign = 1

            while i < len(expr):
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1

                num = 0
                has_num = False

                while i < len(expr) and expr[i].isdigit():
                    num = num * 10 + int(expr[i])
                    has_num = True
                    i += 1

                if i < len(expr) and expr[i] == 'x':
                    coef += sign * (num if has_num else 1)
                    i += 1
                else:
                    const += sign * num

            return coef, const

        left, right = equation.split('=')

        lx, lc = parse(left)
        rx, rc = parse(right)

        coef = lx - rx
        const = rc - lc

        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            return "No solution"

        return f"x={const // coef}"