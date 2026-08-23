# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

# Example 1:

# Input: n = 3
# Output: 3
# Example 2:

# Input: n = 11
# Output: 0
# Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

# Constraints:

# 1 <= n <= 231 - 1






# Brute force:
class Solution:
    def findNthDigit(self, n: int) -> int:
        num = 1

        while n > len(str(num)):
            n -= len(str(num))
            num += 1

        return int(str(num)[n - 1])








# Optimal:
class Solution:
    def findNthDigit(self, n: int) -> int:

        digits = 1
        count = 9
        start = 1

        # Find the digit-length block
        while n > digits * count:
            n -= digits * count

            digits += 1
            count *= 10
            start *= 10

        # Find the actual number
        number = start + (n - 1) // digits

        # Find digit inside that number
        index = (n - 1) % digits

        return int(str(number)[index])