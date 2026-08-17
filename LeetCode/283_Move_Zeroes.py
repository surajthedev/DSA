# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1








# Brute force:
class Solution:
    def moveZeroes(self, nums):
        non_zero = []

        # Non-zero elements collect karo
        for num in nums:
            if num != 0:
                non_zero.append(num)

        # Original array modify karo
        for i in range(len(non_zero)):
            nums[i] = non_zero[i]

        # Baaki positions mein 0
        for i in range(len(non_zero), len(nums)):
            nums[i] = 0






# Optimal:
class Solution:
    def moveZeroes(self, nums):
        insert = 0

        # Saare non-zero elements front mein le aao
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1