# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

# Example 1:

# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Example 2:

# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
 

# Constraints:

# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -105 <= nums[i][j] <= 105
# nums[i] is sorted in non-decreasing order.








# Solution:
import heapq

class Solution:
    def smallestRange(self, nums):
        heap = []
        current_max = float("-inf")

        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))
            current_max = max(current_max, val)

        best_left = heap[0][0]
        best_right = current_max

        while len(heap) == len(nums):
            current_min, list_idx, element_idx = heapq.heappop(heap)

            if (current_max - current_min < best_right - best_left or
                (current_max - current_min == best_right - best_left and
                 current_min < best_left)):
                best_left = current_min
                best_right = current_max

            next_idx = element_idx + 1

            if next_idx == len(nums[list_idx]):
                break

            next_val = nums[list_idx][next_idx]
            heapq.heappush(heap, (next_val, list_idx, next_idx))
            current_max = max(current_max, next_val)

        return [best_left, best_right]