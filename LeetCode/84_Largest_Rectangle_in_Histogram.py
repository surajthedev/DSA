# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104



# Brute force:
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        max_area = 0

        for i in range(n):
            min_height = float('inf')

            for j in range(i, n):
                min_height = min(min_height, heights[j])

                width = j - i + 1
                area = min_height * width

                max_area = max(max_area, area)

        return max_area






# Optimal:
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i, h in enumerate(heights):

            # Current bar is smaller than stack top
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        # Process remaining bars
        n = len(heights)

        while stack:
            height = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            area = height * width
            max_area = max(max_area, area)

        return max_area