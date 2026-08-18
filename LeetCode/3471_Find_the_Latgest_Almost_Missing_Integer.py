# You are given an integer array nums and an integer k.

# An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

# Return the largest almost missing integer from nums. If no such integer exists, return -1.

# A subarray is a contiguous sequence of elements within an array.
 

# Example 1:

# Input: nums = [3,9,2,1,7], k = 3

# Output: 7

# Explanation:

# 1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
# 2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
# 3 appears in 1 subarray of size 3: [3, 9, 2].
# 7 appears in 1 subarray of size 3: [2, 1, 7].
# 9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
# We return 7 since it is the largest integer that appears in exactly one subarray of size k.

# Example 2:

# Input: nums = [3,9,7,2,1,7], k = 4

# Output: 3

# Explanation:

# 1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
# 2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
# 3 appears in 1 subarray of size 4: [3, 9, 7, 2].
# 7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
# 9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
# We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

# Example 3:

# Input: nums = [0,0], k = 1

# Output: -1

# Explanation:

# There is no integer that appears in only one subarray of size 1.

 

# Constraints:

# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 1 <= k <= nums.length







# Brute force:
class Solution:
    def largestInteger(self, nums, k):
        count = {}

        # Har size-k subarray
        for i in range(len(nums) - k + 1):
            seen = set()

            # Current subarray ke elements
            for j in range(i, i + k):
                seen.add(nums[j])

            # Har unique element ko count karo
            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans






# Optimal:
class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        ans = -1

        for x in range(51):
            diff = [0] * (n - k + 2)

            # For every occurrence of x,
            # find all windows that contain it
            for i in range(n):
                if nums[i] == x:
                    left = max(0, i - k + 1)
                    right = min(i, n - k)

                    diff[left] += 1
                    diff[right + 1] -= 1

            # Count how many windows contain x
            count = 0
            current = 0

            for i in range(n - k + 1):
                current += diff[i]

                if current > 0:
                    count += 1

            if count == 1:
                ans = max(ans, x)

        return ans