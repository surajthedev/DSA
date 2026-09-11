# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105








# Brute force:
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            original = nums[i]

            # Try modifying nums[i] to nums[i-1]
            if i == 0:
                nums[i] = nums[i + 1]
            elif i == n - 1:
                nums[i] = nums[i - 1]
            else:
                nums[i] = nums[i - 1]

            valid = True

            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    valid = False
                    break

            nums[i] = original

            if valid:
                return True

        return False







# Optimal:
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changes = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                changes += 1

                if changes > 1:
                    return False

                if i == 1 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True