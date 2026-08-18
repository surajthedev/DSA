# You are given an array of integers distance.

# You start at the point (0, 0) on an X-Y plane, and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

# Return true if your path crosses itself or false if it does not.

 

# Example 1:


# Input: distance = [2,1,1,2]
# Output: true
# Explanation: The path crosses itself at the point (0, 1).
# Example 2:


# Input: distance = [1,2,3,4]
# Output: false
# Explanation: The path does not cross itself at any point.
# Example 3:


# Input: distance = [1,1,1,2,1]
# Output: true
# Explanation: The path crosses itself at the point (0, 0).
 

# Constraints:

# 1 <= distance.length <= 105
# 1 <= distance[i] <= 105





# Brute force:
class Solution:
    def isSelfCrossing(self, distance):
        x = 0
        y = 0
        segments = []

        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        for i, d in enumerate(distance):
            dx, dy = directions[i % 4]

            nx = x + dx * d
            ny = y + dy * d

            segments.append((x, y, nx, ny))

            # Current segment ko previous non-adjacent
            # segments se check karo
            for j in range(len(segments) - 2):
                if self.intersect(segments[j], segments[-1]):
                    return True

            x, y = nx, ny

        return False

    def intersect(self, a, b):
        x1, y1, x2, y2 = a
        x3, y3, x4, y4 = b

        # First segment vertical
        if x1 == x2:
            return (
                x3 <= x1 <= x4 or x4 <= x1 <= x3
            ) and (
                y1 <= y3 <= y2 or y2 <= y3 <= y1
            )

        # First segment horizontal
        return (
            x1 <= x3 <= x2 or x2 <= x3 <= x1
        ) and (
            y3 <= y1 <= y4 or y4 <= y1 <= y3
        )






# Optimal:
class Solution:
    def isSelfCrossing(self, d):
        for i in range(3, len(d)):

            # Case 1:
            # Current line crosses line 3 steps before
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True

            # Case 2:
            # Current line touches/crosses line 4 steps before
            if i >= 4:
                if (
                    d[i - 1] == d[i - 3]
                    and d[i] + d[i - 4] >= d[i - 2]
                ):
                    return True

            # Case 3:
            # Current line crosses line 5 steps before
            if i >= 5:
                if (
                    d[i - 2] >= d[i - 4]
                    and d[i] + d[i - 4] >= d[i - 2]
                    and d[i - 1] <= d[i - 3]
                    and d[i - 1] + d[i - 5] >= d[i - 3]
                ):
                    return True

        return False