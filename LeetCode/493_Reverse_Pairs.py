# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -231 <= nums[i] <= 231 - 1








# Brute force:
class Solution:
    def reversePairs(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    count += 1

        return count







# Optimal:
class Solution:
    def reversePairs(self, nums):
        def merge_sort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid)
            count += merge_sort(mid + 1, right)

            j = mid + 1

            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1

                count += j - (mid + 1)

            nums[left:right + 1] = sorted(nums[left:right + 1])

            return count

        return merge_sort(0, len(nums) - 1)