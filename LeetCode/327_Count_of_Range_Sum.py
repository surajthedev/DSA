# Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

 

# Example 1:

# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
# Example 2:

# Input: nums = [0], lower = 0, upper = 0
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# -105 <= lower <= upper <= 105
# The answer is guaranteed to fit in a 32-bit integer.






# Brute force:
class Solution:
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        count = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                range_sum = prefix[j] - prefix[i]

                if lower <= range_sum <= upper:
                    count += 1

        return count






# Optimal:
class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2

            left, count_left = merge_sort(arr[:mid])
            right, count_right = merge_sort(arr[mid:])

            count = count_left + count_right

            # Count valid pairs
            j = 0
            k = 0

            for x in left:
                while j < len(right) and right[j] - x < lower:
                    j += 1

                while k < len(right) and right[k] - x <= upper:
                    k += 1

                count += k - j

            # Merge sorted arrays
            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count

        _, answer = merge_sort(prefix)

        return answer