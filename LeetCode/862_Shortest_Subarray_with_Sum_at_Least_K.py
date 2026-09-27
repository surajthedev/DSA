# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

# A subarray is a contiguous part of an array.



# Example 1:

# Input: nums = [1], k = 1
# Output: 1
# Example 2:

# Input: nums = [1,2], k = 4
# Output: -1
# Example 3:

# Input: nums = [2,-1,2], k = 3
# Output: 3


# Constraints:

# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 109
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
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]

                if total >= k:
                    ans = min(ans, j - i + 1)

        return -1 if ans == float('inf') else ans










# Optimal:
from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        ans = n + 1

        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return -1 if ans == n + 1 else ans
