# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400





# Brute force:
class Solution:
    def rob(self, nums):
        memo = {}

        def solve(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob = nums[i] + solve(i + 2)
            skip = solve(i + 1)

            memo[i] = max(rob, skip)

            return memo[i]

        return solve(0)








# Optimal:
class Solution:
    def rob(self, nums):
        prev2 = 0
        prev1 = 0

        for money in nums:
            current = max(
                prev1,
                prev2 + money
            )

            prev2 = prev1
            prev1 = current

        return prev1