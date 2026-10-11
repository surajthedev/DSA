# Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

# A subarray is a contiguous part of an array.



# Example 1:

# Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
# Example 2:

# Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
# Example 3:

# Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.


# Constraints:

# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000
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
# ### Brute Force

python
```
class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n - firstLen + 1):
            sum1 = sum(nums[i:i + firstLen])

            for j in range(n - secondLen + 1):
                if i + firstLen <= j or j + secondLen <= i:
                    sum2 = sum(nums[j:j + secondLen])
                    ans = max(ans, sum1 + sum2)

        return ans
```

### Optimal (Prefix Sum)

python
```
class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        def solve(L, M):
            n = len(nums)
            prefix = [0] * (n + 1)

            for i in range(n):
                prefix[i + 1] = prefix[i] + nums[i]

            maxL = 0
            ans = 0

            for i in range(L + M, n + 1):
                l_sum = prefix[i - M] - prefix[i - M - L]
                maxL = max(maxL, l_sum)

                m_sum = prefix[i] - prefix[i - M]
                ans = max(ans, maxL + m_sum)

            return ans

        return max(
            solve(firstLen, secondLen),
            solve(secondLen, firstLen)
        )
```
