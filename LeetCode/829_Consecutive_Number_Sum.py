# Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.



# Example 1:

# Input: n = 5
# Output: 2
# Explanation: 5 = 2 + 3
# Example 2:

# Input: n = 9
# Output: 3
# Explanation: 9 = 4 + 5 = 2 + 3 + 4
# Example 3:

# Input: n = 15
# Output: 4
# Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5


# Constraints:

# 1 <= n <= 109
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def consecutiveNumbersSum(self, n):
        count = 0

        for start in range(1, n + 1):
            total = 0

            for x in range(start, n + 1):
                total += x

                if total == n:
                    count += 1
                    break

                if total > n:
                    break

        return count










# Optimal:
class Solution:
    def consecutiveNumbersSum(self, n):
        count = 0
        k = 1

        while k * (k + 1) // 2 <= n:
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1

            k += 1

        return count
