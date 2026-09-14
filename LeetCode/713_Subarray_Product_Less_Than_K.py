# You are given an array of integers nums and an integer k.

# Return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106






# Brute force:
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        n = len(nums)

        for i in range(n):
            product = 1

            for j in range(i, n):
                product *= nums[j]

                if product < k:
                    count += 1
                else:
                    break

        return count








# Optimal:
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            count += right - left + 1

        return count
