# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

# Constraints:

# 1 <= n <= 231 - 1







# Brute force:
class Solution:
    def hammingWeight(self, n):
        binary = bin(n)[2:]

        count = 0

        for bit in binary:
            if bit == '1':
                count += 1

        return count








# Optimal:
class Solution:
    def hammingWeight(self, n):
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count