# An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

# Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 

# Example 1:

# Input: n = 10
# Output: 9
# Example 2:

# Input: n = 1234
# Output: 1234
# Example 3:

# Input: n = 332
# Output: 299
 

# Constraints:

# 0 <= n <= 109









# Brute force:
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        while n >= 0:
            s = str(n)

            if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
                return n

            n -= 1

        return 0









# Optimal:
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        mark = len(digits)

        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                mark = i

        for i in range(mark, len(digits)):
            digits[i] = '9'

        return int(''.join(digits))