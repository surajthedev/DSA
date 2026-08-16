# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length







# Brute force:
class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []

        for i in range(len(nums) - k + 1):
            window_max = nums[i]

            for j in range(i, i + k):
                window_max = max(window_max, nums[j])

            result.append(window_max)

        return result






# Optimal:
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):

            # Remove elements outside the window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Window size is k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result