# You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

# sumOdd: the sum of the smallest n positive odd numbers.

# sumEven: the sum of the smallest n positive even numbers.

# Return the GCD of sumOdd and sumEven.

 

# Example 1:

# Input: n = 4

# Output: 4

# Explanation:

# Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
# Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
# Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

# Example 2:

# Input: n = 5

# Output: 5

# Explanation:

# Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25
# Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30
# Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5.

 

# Constraints:

# 1 <= n <= 10​​​​​​​00


# Brute Force Solution:
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 0
        even_sum = 0

        # Sum of first n odd numbers
        odd = 1
        for _ in range(n):
            odd_sum += odd
            odd += 2

        # Sum of first n even numbers
        even = 2
        for _ in range(n):
            even_sum += even
            even += 2

        # GCD using Euclidean algorithm
        while even_sum:
            odd_sum, even_sum = even_sum, odd_sum % even_sum

        return odd_sum



# Better Solution:
import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = n * n
        even_sum = n * (n + 1)

        return math.gcd(odd_sum, even_sum)




# Optimal Solution:
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n