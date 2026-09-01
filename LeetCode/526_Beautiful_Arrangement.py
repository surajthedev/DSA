# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 15




# Brute force:
from itertools import permutations

class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0

        for perm in permutations(range(1, n + 1)):
            valid = True

            for i in range(1, n + 1):
                if perm[i - 1] % i != 0 and i % perm[i - 1] != 0:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans







# Optimal:
class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [-1] * (1 << n)

        def dfs(mask):
            if mask == (1 << n) - 1:
                return 1

            if dp[mask] != -1:
                return dp[mask]

            pos = mask.bit_count() + 1
            ans = 0

            for num in range(1, n + 1):
                bit = 1 << (num - 1)

                if mask & bit:
                    continue

                if num % pos == 0 or pos % num == 0:
                    ans += dfs(mask | bit)

            dp[mask] = ans
            return ans

        return dfs(0)