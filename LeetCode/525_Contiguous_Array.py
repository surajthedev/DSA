# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.







# Brute force:
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            zeros = 0
            ones = 0

            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                else:
                    ones += 1

                if zeros == ones:
                    ans = max(ans, j - i + 1)

        return ans









# Optimal:
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        first = {0: -1}
        balance = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1

            if balance in first:
                ans = max(ans, i - first[balance])
            else:
                first[balance] = i

        return ans