# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:


# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
 

# Constraints:

# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.





# Brute force:
class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 2

        for i in range(n):
            for j in range(i + 1, n):

                x1, y1 = points[i]
                x2, y2 = points[j]

                count = 2

                for k in range(n):
                    if k == i or k == j:
                        continue

                    x3, y3 = points[k]

                    # Check if 3 points are collinear
                    if ((y2 - y1) * (x3 - x1) ==
                        (y3 - y1) * (x2 - x1)):
                        count += 1

                ans = max(ans, count)

        return ans








# Optimal:
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = {}

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dy = y2 - y1
                dx = x2 - x1

                # Vertical line
                if dx == 0:
                    slope = (1, 0)

                # Horizontal line
                elif dy == 0:
                    slope = (0, 1)

                else:
                    g = gcd(dy, dx)

                    dy //= g
                    dx //= g

                    # Sign normalize karo
                    if dx < 0:
                        dy = -dy
                        dx = -dx

                    slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

                ans = max(ans, slopes[slope] + 1)

        return ans