# Given a binary array nums, you should delete one element from it.
# 
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
# 
# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 ones.
# 
# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# 
# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
# 
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.

# Brute Force Solution
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            curr_len = 0
            curr_max = 0
            for num in temp:
                if num == 1:
                    curr_len += 1
                    curr_max = max(curr_max, curr_len)
                else:
                    curr_len = 0
            max_len = max(max_len, curr_max)
        return max_len

# Optimal Solution
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            max_len = max(max_len, right - left)
            
        return max_len
