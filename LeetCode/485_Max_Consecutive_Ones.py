# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.









# Brute force:
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ans = 0

        for i in range(len(nums)):
            count = 0

            for j in range(i, len(nums)):
                if nums[j] == 1:
                    count += 1
                    ans = max(ans, count)
                else:
                    break

        return ans





# Optimal:
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0

        return ans

    