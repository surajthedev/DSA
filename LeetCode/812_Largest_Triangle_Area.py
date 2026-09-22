# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.



# Example 1:


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000


# Constraints:

# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.
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
# Brute force:
class Solution:
    def largestTriangleArea(self, points):
        n = len(points)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    ) / 2

                    ans = max(ans, area)

        return ans










# Optimal:
class Solution:
    def largestTriangleArea(self, points):
        ans = 0

        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                for k in range(j + 1, len(points)):
                    x3, y3 = points[k]

                    area = abs(
                        (x2 - x1) * (y3 - y1) -
                        (y2 - y1) * (x3 - x1)
                    )

                    ans = max(ans, area)

        return ans / 2
