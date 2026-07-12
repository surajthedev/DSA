# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in parentheses.
# 
# If multiple answers are possible, return any of them.
# 
# It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.
# 
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# 
# Constraints:
# -2^31 <= numerator, denominator <= 2^31 - 1
# denominator != 0

# Brute Force Solution
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # A brute force approach for decimal expansion using float might lose precision.
        # So we implement the standard division algorithm.
        if numerator == 0: return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        num, den = abs(numerator), abs(denominator)
        res.append(str(num // den))
        rem = num % den
        if rem == 0:
            return "".join(res)
        res.append(".")
        memo = {}
        while rem != 0:
            if rem in memo:
                res.insert(memo[rem], "(")
                res.append(")")
                break
            memo[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den
        return "".join(res)

# Optimal Solution
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        num, den = abs(numerator), abs(denominator)
        res.append(str(num // den))
        rem = num % den
        if rem == 0:
            return "".join(res)
        res.append(".")
        memo = {}
        while rem != 0:
            if rem in memo:
                res.insert(memo[rem], "(")
                res.append(")")
                break
            memo[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den
        return "".join(res)
