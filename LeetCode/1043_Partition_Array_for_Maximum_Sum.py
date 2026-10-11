# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.



# Example 1:

# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# Example 2:

# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# Example 3:

# Input: arr = [1], k = 1
# Output: 1


# Constraints:

# 1 <= arr.length <= 500
# 0 <= arr[i] <= 109
# 1 <= k <= arr.length
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
#
#
#
# ### Brute Force (Recursion + Memoization)

python
```
from functools import lru_cache

class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def solve(i):
            if i == n:
                return 0

            ans = 0
            max_val = 0

            for j in range(i, min(i + k, n)):
                max_val = max(max_val, arr[j])
                length = j - i + 1
                ans = max(ans, max_val * length + solve(j + 1))

            return ans

        return solve(0)
```

### Optimal (Bottom-Up DP)

python
```
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            max_val = 0

            for j in range(i, min(i + k, n)):
                max_val = max(max_val, arr[j])
                length = j - i + 1

                dp[i] = max(
                    dp[i],
                    max_val * length + dp[j + 1]
                )

        return dp[0]
```
