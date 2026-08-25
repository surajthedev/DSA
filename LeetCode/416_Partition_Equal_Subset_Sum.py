# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100





# Brute force:
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        def dfs(i, current_sum):
            if current_sum == target:
                return True

            if i == len(nums) or current_sum > target:
                return False

            # Take nums[i]
            if dfs(i + 1, current_sum + nums[i]):
                return True

            # Don't take nums[i]
            return dfs(i + 1, current_sum)

        return dfs(0, 0)





# Optimal:
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        # Odd total cannot be divided equally
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]