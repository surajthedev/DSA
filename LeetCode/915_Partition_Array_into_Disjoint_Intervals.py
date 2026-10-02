# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.

# Test cases are generated such that partitioning exists.



# Example 1:

# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:

# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]


# Constraints:

# 2 <= nums.length <= 105
# 0 <= nums[i] <= 106
# There is at least one valid answer for the given input.
#
#
#
#
#
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(1, n):
            left_max = max(nums[:i])
            right_min = min(nums[i:])

            if left_max <= right_min:
                return i















# Optimal:
class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        left_max = nums[0]

        for i in range(1, n):
            left_max = max(left_max, nums[i - 1])

            if left_max <= suffix_min[i]:
                return i
