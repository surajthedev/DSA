# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

 

# Example 1:

# Input: nums = [4,14,2]
# Output: 6
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case).
# The answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# Example 2:

# Input: nums = [4,14,4]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 109








# Brute force:
class Solution:
    def totalHammingDistance(self, nums):
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                x = nums[i] ^ nums[j]
                ans += x.bit_count()

        return ans







# Optimal:
class Solution:
    def totalHammingDistance(self, nums):
        ans = 0
        n = len(nums)

        for bit in range(31):
            ones = 0

            for num in nums:
                if num & (1 << bit):
                    ones += 1

            zeros = n - ones
            ans += ones * zeros

        return ans