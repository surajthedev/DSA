# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]
 

# Constraints:

# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1





# Brute force:
class Solution:
    def singleNumber(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = []

        for num, count in freq.items():
            if count == 1:
                result.append(num)

        return result



# Optimal:
class Solution:
    def singleNumber(self, nums):
        xor_all = 0

        # XOR of all numbers
        for num in nums:
            xor_all ^= num

        # Rightmost set bit
        mask = xor_all & -xor_all

        a = 0
        b = 0

        # Divide numbers into two groups
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num

        return [a, b]