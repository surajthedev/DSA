# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

# Example 1:

# Input: expression = "-1/2+1/2"
# Output: "0/1"
# Example 2:

# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:

# Input: expression = "1/3-1/2"
# Output: "-1/6"
 

# Constraints:

# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1, 10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.









# Brute force:
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = Fraction(0, 1)

        i = 0
        while i < len(expression):
            sign = 1

            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            j = expression.find('/', i)
            k = j + 1

            while k < len(expression) and expression[k].isdigit():
                k += 1

            numerator = int(expression[i:j]) * sign
            denominator = int(expression[j + 1:k])

            result += Fraction(numerator, denominator)
            i = k

        return f"{result.numerator}/{result.denominator}"







# Optimal:
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1
        i = 0
        n = len(expression)

        while i < n:
            sign = 1

            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            j = i
            while expression[j].isdigit():
                j += 1

            numerator = sign * int(expression[i:j])

            i = j + 1

            j = i
            while j < n and expression[j].isdigit():
                j += 1

            denominator = int(expression[i:j])

            num = num * denominator + numerator * den
            den *= denominator

            g = gcd(abs(num), den)
            num //= g
            den //= g

            i = j

        return f"{num}/{den}"