# An array is squareful if the sum of every pair of adjacent elements is a perfect square.

# Given an integer array nums, return the number of permutations of nums that are squareful.

# Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].



# Example 1:

# Input: nums = [1,17,8]
# Output: 2
# Explanation: [1,8,17] and [17,8,1] are the valid permutations.
# Example 2:

# Input: nums = [2,2,2]
# Output: 1


# Constraints:

# 1 <= nums.length <= 12
# 0 <= nums[i] <= 109
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
# ### Brute Force

python
```

import itertools
import math
from collections import Counter

class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        count = 0

        for perm in set(itertools.permutations(nums)):
            valid = True

            for i in range(len(perm) - 1):
                s = perm[i] + perm[i + 1]
                root = math.isqrt(s)

                if root * root != s:
                    valid = False
                    break

            if valid:
                count += 1

        return count
```

### Optimal — Backtracking + Memoization

python
```

from collections import Counter
from functools import lru_cache
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        graph = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                s = nums[i] + nums[j]
                root = isqrt(s)
                graph[i][j] = root * root == s

        @lru_cache(None)
        def dfs(mask, last):
            if mask == (1 << n) - 1:
                return 1

            ans = 0
            used = set()

            for i in range(n):
                if mask & (1 << i) or nums[i] in used:
                    continue

                if last != -1 and not graph[last][i]:
                    continue

                used.add(nums[i])
                ans += dfs(mask | (1 << i), i)

            return ans

        return dfs(0, -1)
```
