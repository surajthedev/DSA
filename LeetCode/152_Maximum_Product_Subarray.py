# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.





# Brute force:
class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        ans = nums[0]

        for i in range(n):
            product = 1

            for j in range(i, n):
                product *= nums[j]

                ans = max(ans, product)

        return ans







# Optimal:
class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]

        answer = nums[0]

        for num in nums[1:]:

            # Negative number max/min ko swap kar sakta hai
            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            answer = max(answer, current_max)

        return answer