# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.



# Example 1:


# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:


# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2


# Constraints:

# 1 <= points.length <= 500
# points[i].length == 2
# 0 <= xi, yi <= 4 * 104
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
#
#
# # Brute Force
class Solution:
    def minAreaRect(self, points):
        point_set = set(map(tuple, points))
        ans = float("inf")

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    ans = min(ans, area)

        return 0 if ans == float("inf") else ans











# Optimal
class Solution:
    def minAreaRect(self, points):
        columns = {}

        for x, y in points:
            columns.setdefault(x, []).append(y)

        ans = float("inf")
        last_x = {}

        for x in sorted(columns):
            ys = sorted(columns[x])

            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    y1, y2 = ys[i], ys[j]

                    if (y1, y2) in last_x:
                        width = x - last_x[(y1, y2)]
                        height = y2 - y1
                        ans = min(ans, width * height)

                    last_x[(y1, y2)] = x

        return 0 if ans == float("inf") else ans
