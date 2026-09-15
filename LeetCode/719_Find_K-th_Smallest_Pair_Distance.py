# The distance of a pair of integers a and b is defined as the absolute difference between a and b.

# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

# Example 1:

# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Example 2:

# Input: nums = [1,1,1], k = 2
# Output: 0
# Example 3:

# Input: nums = [1,6,1], k = 3
# Output: 5
 

# Constraints:

# n == nums.length
# 2 <= n <= 104
# 0 <= nums[i] <= 106
# 1 <= k <= n * (n - 1) / 2












# Brute Force
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        distances = []

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                distances.append(abs(nums[i] - nums[j]))

        distances.sort()

        return distances[k - 1]










# Optimal - Sorting + Binary Search
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count_pairs(max_dist):
            count = 0
            left = 0

            for right in range(n):
                while nums[right] - nums[left] > max_dist:
                    left += 1

                count += right - left

            return count

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
