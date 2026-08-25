# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

# Example 1:

# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
# Example 2:

# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
 

# Constraints:

# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 231 - 1







# Brute force:
class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_xor = max(max_xor, nums[i] ^ nums[j])

        return max_xor







# Optimal:
class Solution:
    def findMaximumXOR(self, nums):
        ans = 0
        mask = 0

        # 31 bits: numbers can be up to 2^31 - 1
        for bit in range(30, -1, -1):
            mask |= (1 << bit)

            prefixes = set()

            for num in nums:
                prefixes.add(num & mask)

            candidate = ans | (1 << bit)

            for prefix in prefixes:
                if (prefix ^ candidate) in prefixes:
                    ans = candidate
                    break

        return ans