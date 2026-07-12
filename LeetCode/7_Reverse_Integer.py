# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# 
# Example 1:
# Input: x = 123
# Output: 321
# 
# Example 2:
# Input: x = -123
# Output: -321
# 
# Example 3:
# Input: x = 120
# Output: 21
# 
# Constraints:
# -2^31 <= x <= 2^31 - 1

# Brute Force Solution
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
            
        str_x = str(abs(x))
        reversed_str = str_x[::-1]
        result = int(reversed_str)
        
        if x < 0:
            result = -result
            
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result

# Optimal Solution
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        res = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7):
                return 0
                
            res = res * 10 + pop
            
        return sign * res
