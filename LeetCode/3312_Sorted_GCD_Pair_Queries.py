# You are given an integer array nums of length n and an integer array queries.

# Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

# For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

# Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

# The term gcd(a, b) denotes the greatest common divisor of a and b.

 

# Example 1:

# Input: nums = [2,3,4], queries = [0,2,2]

# Output: [1,2,2]

# Explanation:

# gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].

# After sorting in ascending order, gcdPairs = [1, 1, 2].

# So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].

# Example 2:

# Input: nums = [4,4,2,1], queries = [5,3,1,0]

# Output: [4,2,1,1]

# Explanation:

# gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].

# Example 3:

# Input: nums = [2,2], queries = [0,0]

# Output: [2,2]

# Explanation:

# gcdPairs = [2].

 

# Constraints:

# 2 <= n == nums.length <= 105
# 1 <= nums[i] <= 5 * 104
# 1 <= queries.length <= 105
# 0 <= queries[i] < n * (n - 1) / 2


# Brute Force Solution:
from math import gcd
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        gcds = []

        n = len(nums)

        # Find GCD of every pair
        for i in range(n):
            for j in range(i + 1, n):
                gcds.append(gcd(nums[i], nums[j]))

        # Sort all GCD values
        gcds.sort()

        # Answer queries
        ans = []
        for q in queries:
            ans.append(gcds[q])

        return ans






# Optimal Solution:
from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)

        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                cnt[d] += freq[m]

        # exact[d] = pairs whose gcd is exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2

            multiple = 2 * d
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d

            exact[d] = pairs

        # Prefix sums
        prefix = []
        total = 0

        for d in range(1, mx + 1):
            total += exact[d]
            prefix.append(total)

        ans = []

        for q in queries:
            ans.append(bisect_left(prefix, q + 1) + 1)

        return ans