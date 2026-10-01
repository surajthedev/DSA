# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.



# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.


# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
#
#
#
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(1, n):
            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key

        return nums














# Optimal:
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i, j = left, mid

            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i < mid:
                temp.append(nums[i])
                i += 1

            while j < right:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[left + k] = temp[k]

        merge_sort(0, len(nums))
        return nums
