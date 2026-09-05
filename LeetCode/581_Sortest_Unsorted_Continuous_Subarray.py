# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105







# Brute force:
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = n

        for l in range(n):
            temp = nums[:]

            for r in range(l, n):
                temp[l:r + 1] = sorted(temp[l:r + 1])

                if all(temp[i] <= temp[i + 1] for i in range(n - 1)):
                    ans = min(ans, r - l + 1)
                    break

        return 0 if ans == n else ans









# Optimal:
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        left = -1
        right = -1

        max_seen = nums[0]

        for i in range(1, n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]

        if right == -1:
            return 0

        min_seen = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]

        return right - left + 1