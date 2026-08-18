# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

# Example 1:

# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Example 2:

# Input: nums = [-1]
# Output: [0]
# Example 3:

# Input: nums = [-1,-1]
# Output: [0,0]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104








# Brute force:
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        counts = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    counts[i] += 1

        return counts






# Optimal:
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        counts = [0] * n

        # (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i = left
            j = mid
            right_smaller = 0

            while i < mid and j < right:
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    right_smaller += 1
                    j += 1
                else:
                    temp.append(arr[i])
                    counts[arr[i][1]] += right_smaller
                    i += 1

            while i < mid:
                temp.append(arr[i])
                counts[arr[i][1]] += right_smaller
                i += 1

            while j < right:
                temp.append(arr[j])
                j += 1

            for k in range(len(temp)):
                arr[left + k] = temp[k]

        merge_sort(0, n)

        return counts