# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.



# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length
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
# ## Brute Force — `O(n²)`

```
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        count = 0
        n = len(nums)

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])

                if len(distinct) == k:
                    count += 1
                elif len(distinct) > k:
                    break

        return count
```

## Optimal — Sliding Window — `O(n)`

```
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            freq = {}
            left = 0
            count = 0

            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while len(freq) > k:
                    freq[nums[left]] -= 1

                    if freq[nums[left]] == 0:
                        del freq[nums[left]]

                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)
```
