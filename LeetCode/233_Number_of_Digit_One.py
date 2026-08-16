# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

# Example 1:

# Input: n = 13
# Output: 6
# Example 2:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 109




# Brute force:
class Solution:
    def countDigitOne(self, n):
        count = 0

        for num in range(1, n + 1):
            while num > 0:
                if num % 10 == 1:
                    count += 1

                num //= 10

        return count




# Optimal:
class Solution:
    def countDigitOne(self, n):
        count = 0
        factor = 1

        while factor <= n:
            high = n // (factor * 10)
            cur = (n // factor) % 10
            low = n % factor

            if cur == 0:
                count += high * factor

            elif cur == 1:
                count += high * factor + low + 1

            else:
                count += (high + 1) * factor

            factor *= 10

        return count