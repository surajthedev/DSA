# Given an integer n, return the smallest prime palindrome greater than or equal to n.

# An integer is prime if it has exactly two divisors: 1 and itself. Note that 1 is not a prime number.

# For example, 2, 3, 5, 7, 11, and 13 are all primes.
# An integer is a palindrome if it reads the same from left to right as it does from right to left.

# For example, 101 and 12321 are palindromes.
# The test cases are generated so that the answer always exists and is in the range [2, 2 * 108].



# Example 1:

# Input: n = 6
# Output: 7
# Example 2:

# Input: n = 8
# Output: 11
# Example 3:

# Input: n = 13
# Output: 101


# Constraints:

# 1 <= n <= 108
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
    def primePalindrome(self, n: int) -> int:

        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]

        def is_prime(x):
            if x < 2:
                return False

            if x % 2 == 0:
                return x == 2

            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2

            return True

        while True:
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1








# Optimal:
class Solution:
    def primePalindrome(self, n: int) -> int:

        def is_prime(x):
            if x < 2:
                return False

            if x % 2 == 0:
                return x == 2

            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2

            return True

        # 8-digit palindromes are always divisible by 11
        if 8 <= n <= 11:
            return 11

        length = len(str(n))

        while True:
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len

            for half in range(start, end):
                s = str(half)

                # Generate palindrome
                if length % 2:
                    pal = int(s + s[-2::-1])
                else:
                    pal = int(s + s[::-1])

                if pal >= n and is_prime(pal):
                    return pal

            length += 1
