# Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

 

# Example 1:

# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
# Example 2:

# Input: n = 1
# Output: 2
# Example 3:

# Input: n = 2
# Output: 3
 

# Constraints:

# 1 <= n <= 109






# Brute force:
class Solution:
    def findIntegers(self, n: int) -> int:
        ans = 0

        for i in range(n + 1):
            binary = bin(i)[2:]

            if "11" not in binary:
                ans += 1

        return ans








# Optimal:
class Solution:
    def findIntegers(self, n: int) -> int:
        bits = bin(n)[2:]
        m = len(bits)

        dp = [0] * (m + 1)
        dp[0] = 1
        dp[1] = 2

        for i in range(2, m + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        ans = 0

        for i in range(m):
            if bits[i] == '1':
                ans += dp[m - i - 1]

                if i > 0 and bits[i - 1] == '1':
                    return ans

        return ans + 1



