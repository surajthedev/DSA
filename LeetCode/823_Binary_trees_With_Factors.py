# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.



# Example 1:

# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:

# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


# Constraints:

# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109
# All the values of arr are unique.
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        nums = set(arr)

        from functools import lru_cache

        @lru_cache(None)
        def dp(root):
            count = 1

            for a in arr:
                if root % a == 0:
                    b = root // a

                    if b in nums:
                        count += dp(a) * dp(b)

            return count

        return sum(dp(x) for x in arr) % MOD









# Optimal:
class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()

        dp = {x: 1 for x in arr}

        for i in range(len(arr)):
            x = arr[i]

            for j in range(i):
                a = arr[j]

                if x % a == 0:
                    b = x // a

                    if b in dp:
                        dp[x] = (dp[x] + dp[a] * dp[b]) % MOD

        return sum(dp.values()) % MOD
