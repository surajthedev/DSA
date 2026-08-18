# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).
 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 




# Brute force:
class Solution:
    def countBits(self, n):
        ans = []

        for num in range(n + 1):
            count = 0
            x = num

            while x > 0:
                count += x % 2
                x //= 2

            ans.append(count)

        return ans






# Optimal:
class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans