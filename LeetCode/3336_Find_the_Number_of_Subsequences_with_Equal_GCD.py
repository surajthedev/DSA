# You are given an integer array nums.

# Your task is to find the number of pairs of non-empty subsequences (seq1, seq2) of nums that satisfy the following conditions:

# The subsequences seq1 and seq2 are disjoint, meaning no index of nums is common between them.
# The GCD of the elements of seq1 is equal to the GCD of the elements of seq2.
# Return the total number of such pairs.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 10

# Explanation:

# The subsequence pairs which have the GCD of their elements equal to 1 are:

# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# Example 2:

# Input: nums = [10,20,30]

# Output: 2

# Explanation:

# The subsequence pairs which have the GCD of their elements equal to 10 are:

# ([10, 20, 30], [10, 20, 30])
# ([10, 20, 30], [10, 20, 30])
# Example 3:

# Input: nums = [1,1,1,1]

# Output: 50

 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 200



# Brute Force:
from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        ans = 0

        def dfs(i, g1, g2, used1, used2):
            nonlocal ans

            if i == n:
                if used1 and used2 and g1 == g2:
                    ans = (ans + 1) % MOD
                return

            # Ignore
            dfs(i + 1, g1, g2, used1, used2)

            # Put in first subsequence
            ng1 = nums[i] if not used1 else gcd(g1, nums[i])
            dfs(i + 1, ng1, g2, True, used2)

            # Put in second subsequence
            ng2 = nums[i] if not used2 else gcd(g2, nums[i])
            dfs(i + 1, g1, ng2, used1, True)

        dfs(0, 0, 0, False, False)
        return ans


# Optimized DP:
from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        M = max(nums)

        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [row[:] for row in dp]

            for g1 in range(M + 1):
                for g2 in range(M + 1):
                    if dp[g1][g2] == 0:
                        continue

                    # Put x in first subsequence
                    ng1 = x if g1 == 0 else gcd(g1, x)
                    ndp[ng1][g2] = (ndp[ng1][g2] + dp[g1][g2]) % MOD

                    # Put x in second subsequence
                    ng2 = x if g2 == 0 else gcd(g2, x)
                    ndp[g1][ng2] = (ndp[g1][ng2] + dp[g1][g2]) % MOD

            dp = ndp

        ans = 0
        for g in range(1, M + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans