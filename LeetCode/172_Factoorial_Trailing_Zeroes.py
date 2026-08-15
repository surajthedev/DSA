# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 104





# Brute force:
class Solution:
    def trailingZeroes(self, n):
        factorial = 1

        for i in range(1, n + 1):
            factorial *= i

        count = 0

        while factorial % 10 == 0:
            count += 1
            factorial //= 10

        return count











# Optimal:
class Solution:
    def trailingZeroes(self, n):
        count = 0

        while n > 0:
            n //= 5
            count += n

        return count