# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.

 

# Example 1:

# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# Example 2:

# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5000
# It is guaranteed that there will be an answer for the given input nums.






# Brute force:
class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)

        n = len(nums)
        mid = (n + 1) // 2

        small = arr[:mid][::-1]
        large = arr[mid:][::-1]

        i = 0

        for x in small:
            nums[i] = x
            i += 2

        i = 1

        for x in large:
            nums[i] = x
            i += 2







# Optimal:
class Solution:
    def wiggleSort(self, nums):
        n = len(nums)

        # Find median
        arr = sorted(nums)
        median = arr[n // 2]

        def index(i):
            return (1 + 2 * i) % (n | 1)

        left = 0
        i = 0
        right = n - 1

        while i <= right:

            if nums[index(i)] > median:
                nums[index(left)], nums[index(i)] = \
                    nums[index(i)], nums[index(left)]
                left += 1
                i += 1

            elif nums[index(i)] < median:
                nums[index(i)], nums[index(right)] = \
                    nums[index(right)], nums[index(i)]
                right -= 1

            else:
                i += 1