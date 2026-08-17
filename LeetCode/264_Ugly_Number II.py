# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

 

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

# Constraints:

# 1 <= n <= 1690



# Brute force:
class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False

        for p in (2, 3, 5):
            while num % p == 0:
                num //= p

        return num == 1

    def nthUglyNumber(self, n):
        count = 0
        num = 1

        while count < n:
            if self.isUgly(num):
                count += 1

            if count == n:
                return num

            num += 1






# Optimal:
class Solution:
    def nthUglyNumber(self, n):
        dp = [0] * n
        dp[0] = 1

        i2 = 0
        i3 = 0
        i5 = 0

        for i in range(1, n):
            next2 = dp[i2] * 2
            next3 = dp[i3] * 3
            next5 = dp[i5] * 5

            dp[i] = min(next2, next3, next5)

            # Move every pointer that produced
            # the current ugly number.
            if dp[i] == next2:
                i2 += 1

            if dp[i] == next3:
                i3 += 1

            if dp[i] == next5:
                i5 += 1

        return dp[n - 1]