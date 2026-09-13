# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false
 

# Constraints:

# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 104
# The frequency of each element is in the range [1, 4].









# Brute Force
class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        buckets = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]

                    if backtrack(i + 1):
                        return True

                    buckets[j] -= nums[i]

                if buckets[j] == 0:
                    break

            return False

        return backtrack(0)







# Optimal - Bitmask DP
class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        n = len(nums)

        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue

            for i in range(n):
                if not (mask & (1 << i)):
                    new_sum = dp[mask] + nums[i]

                    if new_sum <= target:
                        new_mask = mask | (1 << i)

                        if new_sum == target:
                            dp[new_mask] = 0
                        else:
                            dp[new_mask] = new_sum

        return dp[-1] == 0