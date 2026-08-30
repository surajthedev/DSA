# Given an integer n, return the largest palindromic integer that can be represented as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

 

# Example 1:

# Input: n = 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
# Example 2:

# Input: n = 1
# Output: 9
 

# Constraints:

# 1 <= n <= 8







# Brute force:
class Solution:
    def largestPalindrome(self, n):
        if n == 1:
            return 9

        high = 10 ** n - 1
        low = 10 ** (n - 1)

        ans = 0

        for i in range(high, low - 1, -1):
            for j in range(i, low - 1, -1):
                product = i * j

                if product <= ans:
                    break

                if str(product) == str(product)[::-1]:
                    ans = product

        return ans % 1337






# Optimal:
class Solution:
    def largestPalindrome(self, n):
        if n == 1:
            return 9

        high = 10 ** n - 1
        low = 10 ** (n - 1)

        half_high = high
        half_low = 10 ** (n - 1)

        for left in range(half_high, half_low - 1, -1):
            palindrome = int(str(left) + str(left)[::-1])

            x = high

            while x * x >= palindrome:
                if palindrome % x == 0:
                    y = palindrome // x

                    if low <= y <= high:
                        return palindrome % 1337

                x -= 1

        return 0