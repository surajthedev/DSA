# The width of a sequence is the difference between the maximum and minimum elements in the sequence.

# Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 109 + 7.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



# Example 1:

# Input: nums = [2,1,3]
# Output: 6
# Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
# Example 2:

# Input: nums = [2]
# Output: 0


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
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
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        ans = 0

        for mask in range(1, 1 << n):
            mn = float('inf')
            mx = float('-inf')

            for i in range(n):
                if mask & (1 << i):
                    mn = min(mn, nums[i])
                    mx = max(mx, nums[i])

            ans = (ans + mx - mn) % MOD

        return ans















# Optimal:
class Solution:
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        nums.sort()

        n = len(nums)
        ans = 0
        power = 1

        for i in range(n):
            ans = (ans + nums[i] * power - nums[i] * pow(2, n - 1 - i, MOD)) % MOD
            power = (power * 2) % MOD

        return ans
