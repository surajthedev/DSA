# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.



# Brute force:
class Solution:
    def sortColors(self, nums: list[int]) -> None:

        count0 = 0
        count1 = 0
        count2 = 0

        # Count
        for x in nums:
            if x == 0:
                count0 += 1
            elif x == 1:
                count1 += 1
            else:
                count2 += 1

        # Fill 0s
        i = 0

        for _ in range(count0):
            nums[i] = 0
            i += 1

        # Fill 1s
        for _ in range(count1):
            nums[i] = 1
            i += 1

        # Fill 2s
        for _ in range(count2):
            nums[i] = 2
            i += 1






# Optimal solution:
class Solution:
    def sortColors(self, nums: list[int]) -> None:

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1