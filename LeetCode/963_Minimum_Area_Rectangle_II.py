# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.

# Answers within 10-5 of the actual answer will be accepted.



# Example 1:


# Input: points = [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
# Example 2:


# Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
# Example 3:


# Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.


# Constraints:

# 1 <= points.length <= 50
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
# Brute force:
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        point_set = {tuple(p) for p in points}
        ans = float("inf")

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):

                        p1 = points[i]
                        p2 = points[j]
                        p3 = points[k]
                        p4 = points[l]

                        # Check all 3 possible diagonal pairings
                        pairs = [
                            (p1, p2, p3, p4),
                            (p1, p3, p2, p4),
                            (p1, p4, p2, p3)
                        ]

                        for a, b, c, d in pairs:
                            if (
                                a[0] + b[0] == c[0] + d[0]
                                and
                                a[1] + b[1] == c[1] + d[1]
                            ):
                                d1 = (
                                    (a[0] - b[0]) ** 2
                                    + (a[1] - b[1]) ** 2
                                )

                                d2 = (
                                    (c[0] - d[0]) ** 2
                                    + (c[1] - d[1]) ** 2
                                )

                                if d1 == d2 and d1 > 0:
                                    area = abs(
                                        (c[0] - a[0]) * (d[1] - a[1])
                                        - (c[1] - a[1]) * (d[0] - a[0])
                                    )

                                    if area > 0:
                                        ans = min(ans, area)

        return 0 if ans == float("inf") else ans












# Optimal:
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        ans = float("inf")

        groups = {}

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # Diagonal midpoint * 2
                mx = x1 + x2
                my = y1 + y2

                # Squared diagonal length
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2

                key = (mx, my, dist)

                if key not in groups:
                    groups[key] = []

                groups[key].append((i, j))

        for pairs in groups.values():
            m = len(pairs)

            for a in range(m):
                i, j = pairs[a]

                for b in range(a + 1, m):
                    k, l = pairs[b]

                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    # Adjacent sides from point i
                    ax = x3 - x1
                    ay = y3 - y1

                    bx = x3 - x2
                    by = y3 - y2

                    # Area = |cross product|
                    area = abs(ax * by - ay * bx)

                    if area > 0:
                        ans = min(ans, area)

        return 0 if ans == float("inf") else ans
