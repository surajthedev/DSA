# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.



# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15


# Constraints:

# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length
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
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]

                if total == goal:
                    ans += 1
                elif total > goal:
                    break

        return ans











# Optimal:
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def at_most(k):
            if k < 0:
                return 0

            left = 0
            total = 0
            count = 0

            for right in range(len(nums)):
                total += nums[right]

                while total > k:
                    total -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return at_most(goal) - at_most(goal - 1)
