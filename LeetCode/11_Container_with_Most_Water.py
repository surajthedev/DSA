# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


# Brute Force Approach
# Idea
# Check every possible pair of lines.
# Calculate the area formed by each pair.
# Keep track of the maximum area.
# The formula for calculating water:
# Area = min(height[left], height[right]) * (right - left)
# Where:
# min(height[left], height[right]) gives the container height.
# (right - left) gives the width.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_water = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):

                width = j - i
                h = min(height[i], height[j])

                area = width * h

                max_water = max(max_water, area)

        return max_water




# Optimal Approach (Two Pointer)
# Idea
# Instead of checking every pair, we use two pointers:
# One pointer starts from the beginning (left).
# One pointer starts from the end (right).
# Calculate the area between them.
# Move the pointer with the smaller height because the smaller height limits the amount of water.
# Steps
# Initialize two pointers:
# left = 0
# right = n - 1
# Calculate the current area:
# Area = min(height[left], height[right]) * (right - left)
# Update the maximum area.
# Move the pointer:
# If height[left] < height[right], move left forward.
# Otherwise, move right backward.


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:

            width = right - left
            h = min(height[left], height[right])

            area = width * h

            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water