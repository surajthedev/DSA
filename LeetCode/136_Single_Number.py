# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# 
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# 
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# 
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# 
# Example 3:
# Input: nums = [1]
# Output: 1
# 
# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears only once.

# Brute Force Solution
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]

# Optimal Solution
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
