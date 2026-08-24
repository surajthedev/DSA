# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= k <= min(50, nums.length)






# Brute force:
class Solution:
    def splitArray(self, nums, k):

        n = len(nums)

        def dfs(start, parts):

            # Last part: remaining elements form one subarray
            if parts == 1:
                return sum(nums[start:])

            current_sum = 0
            ans = float("inf")

            # Leave at least parts-1 elements
            # for remaining subarrays
            for i in range(start, n - parts + 1):

                current_sum += nums[i]

                remaining = dfs(i + 1, parts - 1)

                largest = max(current_sum, remaining)

                ans = min(ans, largest)

            return ans

        return dfs(0, k)







# Optimal:
class Solution:
    def splitArray(self, nums, k):

        left = max(nums)
        right = sum(nums)

        def can_split(max_sum):

            subarrays = 1
            current_sum = 0

            for num in nums:

                if current_sum + num > max_sum:
                    # Start a new subarray
                    subarrays += 1
                    current_sum = num

                    if subarrays > k:
                        return False

                else:
                    current_sum += num

            return True

        while left < right:

            mid = (left + right) // 2

            if can_split(mid):
                # mid is possible
                # Try smaller answer
                right = mid

            else:
                # mid is not possible
                left = mid + 1

        return left