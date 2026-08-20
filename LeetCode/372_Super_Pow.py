# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

 

# Example 1:

# Input: a = 2, b = [3]
# Output: 8
# Example 2:

# Input: a = 2, b = [1,0]
# Output: 1024
# Example 3:

# Input: a = 1, b = [4,3,3,8,5,2]
# Output: 1
 

# Constraints:

# 1 <= a <= 231 - 1
# 1 <= b.length <= 2000
# 0 <= b[i] <= 9
# b does not contain leading zeros.








# Brute force:
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        exponent = 0

        for digit in b:
            exponent = exponent * 10 + digit

        return pow(a, exponent, 1337)







# Optimal:
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        result = 1

        a %= MOD

        for digit in b:
            result = pow(result, 10, MOD)
            result = (result * pow(a, digit, MOD)) % MOD

        return result