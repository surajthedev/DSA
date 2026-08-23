# Given a positive integer n, you can apply one of the following operations:

# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.
# Return the minimum number of operations needed for n to become 1.

 

# Example 1:

# Input: n = 8
# Output: 3
# Explanation: 8 -> 4 -> 2 -> 1
# Example 2:

# Input: n = 7
# Output: 4
# Explanation: 7 -> 8 -> 4 -> 2 -> 1
# or 7 -> 6 -> 3 -> 2 -> 1
# Example 3:

# Input: n = 4
# Output: 2
 

# Constraints:

# 1 <= n <= 231 - 1




# Brute force:
class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}

        def solve(x):
            if x == 1:
                return 0

            if x in memo:
                return memo[x]

            if x % 2 == 0:
                answer = 1 + solve(x // 2)
            else:
                answer = 1 + min(
                    solve(x - 1),
                    solve(x + 1)
                )

            memo[x] = answer
            return answer

        return solve(n)






# Optimal:
class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0

        while n != 1:

            # Even
            if n % 2 == 0:
                n //= 2

            # Odd
            else:
                # Special case
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1

            operations += 1

        return operations