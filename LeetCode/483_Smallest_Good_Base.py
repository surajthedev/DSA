# Given an integer n represented as a string, return the smallest good base of n.

# We call k >= 2 a good base of n, if all digits of n base k are 1's.

 

# Example 1:

# Input: n = "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
# Example 2:

# Input: n = "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
# Example 3:

# Input: n = "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
 

# Constraints:

# n is an integer in the range [3, 1018].
# n does not contain any leading zeros.







# Brute force:
class Solution:
    def smallestGoodBase(self, n):
        n = int(n)

        for k in range(2, n):
            x = n

            while x % k == 1:
                x = (x - 1) // k

            if x == 1:
                return str(k)

        return str(n - 1)








# Optimal:
class Solution:
    def smallestGoodBase(self, n):
        n = int(n)

        max_len = n.bit_length()

        for length in range(max_len, 1, -1):
            left = 2
            right = int(n ** (1 / (length - 1))) + 1

            while left <= right:
                k = (left + right) // 2

                total = 0
                power = 1

                for _ in range(length):
                    total += power

                    if total > n:
                        break

                    power *= k

                if total == n:
                    return str(k)

                if total < n:
                    left = k + 1
                else:
                    right = k - 1

        return str(n - 1)