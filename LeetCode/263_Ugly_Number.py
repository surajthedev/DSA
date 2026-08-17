# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 

# Constraints:

# -231 <= n <= 231 - 1




# Brute force:
class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False

        for i in range(2, n + 1):
            # Check if i is a factor of n
            if n % i == 0:

                # Check whether i is prime
                is_prime = True

                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        is_prime = False
                        break

                # Prime factor other than 2, 3, 5
                if is_prime and i not in (2, 3, 5):
                    return False

        return True






# Optimal:
class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p

        return n == 1