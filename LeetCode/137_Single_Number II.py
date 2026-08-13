# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.







# Brute force:
from collections import Counter

class Solution:
    def singleNumber(self, nums):
        count = Counter(nums)

        for num in nums:
            if count[num] == 1:
                return num








# Optimal:
class Solution:
    def singleNumber(self, nums):
        result = 0

        for bit in range(32):
            count = 0

            for num in nums:
                # Check current bit
                if (num >> bit) & 1:
                    count += 1

            # If this bit appears 1 time modulo 3,
            # it belongs to the single number
            if count % 3:
                result |= (1 << bit)

        # Convert 32-bit unsigned result to signed integer
        if result >= (1 << 31):
            result -= (1 << 32)

        return result