# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
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
# ### Brute Force — O(n²)

python
```

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            zeros = 0

            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1

                if zeros > k:
                    break

                ans = max(ans, j - i + 1)

        return ans
```

### Optimal — Sliding Window, O(n)

python
```

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```
