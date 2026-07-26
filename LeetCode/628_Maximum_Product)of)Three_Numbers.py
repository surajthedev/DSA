# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


# Brute Force Approach:
class Solution:
    def maximumProduct(self, nums):
        n = len(nums)
        max_product = float('-inf')

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    product = nums[i] * nums[j] * nums[k]
                    max_product = max(max_product, product)

        return max_product









# Optimal Approach:
class Solution:
    def maximumProduct(self, nums):

        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:

            # update maximums
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num

            elif num > max2:
                max3 = max2
                max2 = num

            elif num > max3:
                max3 = num


            # update minimums
            if num < min1:
                min2 = min1
                min1 = num

            elif num < min2:
                min2 = num


        return max(
            max1 * max2 * max3,
            min1 * min2 * max1
        )