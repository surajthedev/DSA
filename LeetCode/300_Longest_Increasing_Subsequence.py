# Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104





# Brute force:
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)






# Optimal:
class Solution:
    def lengthOfLIS(self, nums):
        arr = []

        for num in nums:
            left = 0
            right = len(arr)

            while left < right:
                mid = (left + right) // 2

                if arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(arr):
                arr.append(num)
            else:
                arr[left] = num

        return len(arr)