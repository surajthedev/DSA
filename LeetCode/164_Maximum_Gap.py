# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

 

# Example 1:

# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
# Example 2:

# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109






# Brute force:
class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        nums.sort()

        ans = 0

        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i - 1])

        return ans







# Optimal:
class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        # All values same hain
        if min_val == max_val:
            return 0

        # Minimum possible maximum gap
        bucket_size = max(1, (max_val - min_val) // (n - 1))

        # Number of buckets
        bucket_count = (max_val - min_val) // bucket_size + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count

        # Put values into buckets
        for num in nums:
            index = (num - min_val) // bucket_size

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)

        # Find maximum gap between non-empty buckets
        ans = 0
        previous_max = min_val

        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue

            gap = bucket_min[i] - previous_max
            ans = max(ans, gap)

            previous_max = bucket_max[i]

        return ans