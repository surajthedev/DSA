# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

# Example 1:

# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Example 2:

# Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
# Output: [0,2,4]
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] < 216
# 1 <= k <= floor(nums.length / 3)








# Brute Force
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def get_sum(i):
            return prefix[i + k] - prefix[i]

        best = None
        best_sum = -1

        for i in range(n - 3 * k + 1):
            for j in range(i + k, n - 2 * k + 1):
                for l in range(j + k, n - k + 1):
                    total = get_sum(i) + get_sum(j) + get_sum(l)

                    if total > best_sum:
                        best_sum = total
                        best = [i, j, l]

        return best











# Optimal
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)

        window = [0] * (n - k + 1)
        window[0] = sum(nums[:k])

        for i in range(1, len(window)):
            window[i] = window[i - 1] - nums[i - 1] + nums[i + k - 1]

        left = [0] * len(window)
        best = 0

        for i in range(len(window)):
            if window[i] > window[best]:
                best = i
            left[i] = best

        right = [0] * len(window)
        best = len(window) - 1

        for i in range(len(window) - 1, -1, -1):
            if window[i] >= window[best]:
                best = i
            right[i] = best

        ans = []
        max_total = -1

        for j in range(k, len(window) - k):
            i = left[j - k]
            l = right[j + k]

            total = window[i] + window[j] + window[l]

            if total > max_total:
                max_total = total
                ans = [i, j, l]

        return ans