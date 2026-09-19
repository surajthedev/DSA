# You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

# The number of global inversions is the number of the different pairs (i, j) where:

# 0 <= i < j < n
# nums[i] > nums[j]
# The number of local inversions is the number of indices i where:

# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# Return true if the number of global inversions is equal to the number of local inversions.

 

# Example 1:

# Input: nums = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion and 1 local inversion.
# Example 2:

# Input: nums = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions and 1 local inversion.
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i] < n
# All the integers of nums are unique.
# nums is a permutation of all the numbers in the range [0, n - 1].










# Brute force:
class Solution:
    def isIdealPermutation(self, nums):
        n = len(nums)

        global_inv = 0
        local_inv = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    global_inv += 1

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                local_inv += 1

        return global_inv == local_inv














# Optimal:
class Solution:
    def isIdealPermutation(self, nums):
        max_seen = 0

        for i in range(len(nums) - 2):
            max_seen = max(max_seen, nums[i])

            if max_seen > nums[i + 2]:
                return False

        return True