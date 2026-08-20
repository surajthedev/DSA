# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000







# Brute force:
class Solution:
    def getSum(self, a: int, b: int) -> int:

        def increment(x):
            mask = 1

            while x & mask:
                x ^= mask
                mask <<= 1

            x ^= mask
            return x

        def decrement(x):
            mask = 1

            while not (x & mask):
                x ^= mask
                mask <<= 1

            x ^= mask
            return x

        while b != 0:

            if b > 0:
                a = increment(a)
                b = decrement(b)
            else:
                a = decrement(a)
                b = increment(b)

        return a







# Optimal:
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        if a <= MAX_INT:
            return a

        return ~(a ^ MASK)