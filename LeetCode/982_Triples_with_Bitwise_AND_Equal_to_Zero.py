# Given an integer array nums, return the number of AND triples.

# An AND triple is a triple of indices (i, j, k) such that:

# 0 <= i < nums.length
# 0 <= j < nums.length
# 0 <= k < nums.length
# nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.


# Example 1:

# Input: nums = [2,1,3]
# Output: 12
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
# Example 2:

# Input: nums = [0,0,0]
# Output: 27


# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] < 216
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    def countTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (nums[i] & nums[j] & nums[k]) == 0:
                        ans += 1

        return ans















# Optimal:
class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        M = 1 << 16

        freq = [0] * M

        for x in nums:
            freq[x] += 1

        # dp[mask] = number of ordered pairs (a, b)
        # whose AND is a submask of mask.
        dp = [0] * M

        for a in nums:
            for b in nums:
                dp[a & b] += 1

        # SOS DP
        for bit in range(16):
            for mask in range(M):
                if mask & (1 << bit):
                    dp[mask] += dp[mask ^ (1 << bit)]

        ans = 0

        full = M - 1

        for x in nums:
            # Pair AND must be a submask of complement of x.
            ans += dp[full ^ x]

        return ans
