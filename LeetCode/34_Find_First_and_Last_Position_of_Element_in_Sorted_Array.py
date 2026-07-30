# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109






# Brute Force Approach:
class Solution:
    def searchRange(self, nums, target):

        start = -1
        end = -1

        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                end = i

        return [start, end]








# Optimal Approach:
class Solution:
    def searchRange(self, nums, target):

        def search(first):
            low, high = 0, len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid
                    if first:
                        high = mid - 1
                    else:
                        low = mid + 1

                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        return [search(True), search(False)]