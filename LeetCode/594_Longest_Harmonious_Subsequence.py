# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Explanation:

# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0

# Explanation:

# No harmonic subsequence exists.

 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109










# Brute force:
from itertools import combinations

class Solution:
    def findLHS(self, nums):
        n = len(nums)
        ans = 0

        for mask in range(1, 1 << n):
            mn = float('inf')
            mx = float('-inf')
            count = 0

            for i in range(n):
                if mask & (1 << i):
                    mn = min(mn, nums[i])
                    mx = max(mx, nums[i])
                    count += 1

            if mx - mn == 1:
                ans = max(ans, count)

        return ans










# Optimal:
from collections import Counter

class Solution:
    def findLHS(self, nums):
        freq = Counter(nums)
        ans = 0

        for x in freq:
            if x + 1 in freq:
                ans = max(ans, freq[x] + freq[x + 1])

        return ans