# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

 

# Example 1:

# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# Example 2:

# Input: num = 7
# Output: false
 

# Constraints:

# 1 <= num <= 108






# Brute force:
class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        total = 0

        for i in range(1, num):
            if num % i == 0:
                total += i

        return total == num








# Optimal:
class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        total = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

            i += 1

        return total == num