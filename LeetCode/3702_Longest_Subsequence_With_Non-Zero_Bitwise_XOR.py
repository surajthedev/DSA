# You are given an integer array nums.

# Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

 

# Example 1:

# Input: nums = [1,2,3]

# Output: 2

# Explanation:

# One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

# Example 2:

# Input: nums = [2,3,4]

# Output: 3

# Explanation:

# The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109






# Brute force:
def longest_subsequence_brute(nums):
    n = len(nums)
    ans = 0

    # Every possible subsequence represented by a bitmask
    for mask in range(1, 1 << n):
        xor_val = 0
        length = 0

        for i in range(n):
            if mask & (1 << i):
                xor_val ^= nums[i]
                length += 1

        if xor_val != 0:
            ans = max(ans, length)

    return ans









# Optimal:
class Solution:
    def longestSubsequence(self, nums):
        total_xor = 0

        for num in nums:
            total_xor ^= num

        # Whole array ka XOR non-zero hai
        if total_xor != 0:
            return len(nums)

        # XOR zero hai, lekin koi non-zero element hai
        if any(nums):
            return len(nums) - 1

        # Saare elements zero hain
        return 0