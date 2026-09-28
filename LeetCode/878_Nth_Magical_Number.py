# A positive integer is magical if it is divisible by either a or b.

# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.



# Example 1:

# Input: n = 1, a = 2, b = 3
# Output: 2
# Example 2:

# Input: n = 4, a = 2, b = 3
# Output: 6


# Constraints:

# 1 <= n <= 109
# 2 <= a, b <= 4 * 104
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
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        count = 0
        num = 1

        while count < n:
            if num % a == 0 or num % b == 0:
                count += 1

            if count == n:
                return num % (10**9 + 7)

            num += 1

        return -1














# Optimal:
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        lcm = a // gcd(a, b) * b

        left = 1
        right = n * min(a, b)

        while left < right:
            mid = (left + right) // 2

            count = mid // a + mid // b - mid // lcm

            if count >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD
