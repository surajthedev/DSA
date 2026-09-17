# You are given an array of integers arr and an integer target.

# You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

# Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

# Example 1:

# Input: arr = [3,2,2,4,3], target = 3
# Output: 2
# Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
# Example 2:

# Input: arr = [7,3,4,7], target = 7
# Output: 2
# Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
# Example 3:

# Input: arr = [4,3,2,6,2,3,4], target = 6
# Output: -1
# Explanation: We have only one sub-array of sum = 6.
 

# Constraints:

# 1 <= arr.length <= 105
# 1 <= arr[i] <= 1000
# 1 <= target <= 108










# Brute force:
class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        subarrays = []

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += arr[j]

                if total == target:
                    subarrays.append((i, j, j - i + 1))

        ans = float("inf")

        for i in range(len(subarrays)):
            for j in range(i + 1, len(subarrays)):
                l1, r1, len1 = subarrays[i]
                l2, r2, len2 = subarrays[j]

                if r1 < l2 or r2 < l1:
                    ans = min(ans, len1 + len2)

        return -1 if ans == float("inf") else ans














# Optimal:
class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float("inf")

        best = [INF] * n
        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                best[right] = length

            if right > 0:
                best[right] = min(best[right], best[right - 1])

        return -1 if ans == INF else ans