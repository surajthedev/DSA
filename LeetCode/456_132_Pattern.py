# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

# Constraints:

# n == nums.length
# 1 <= n <= 2 * 105
# -109 <= nums[i] <= 109






# Brute force:
class Solution:
    def find132pattern(self, nums):
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] >= nums[j]:
                    continue

                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True

        return False






# Optimal:
class Solution:
    def find132pattern(self, nums):
        stack = []
        second = float("-inf")

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True

            while stack and nums[i] > stack[-1]:
                second = stack.pop()

            stack.append(nums[i])

        return False