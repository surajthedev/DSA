# You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.

# Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.

# Return the total area. Since the answer may be too large, return it modulo 109 + 7.



# Example 1:


# Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
# From (1,1) to (2,2), the green and red rectangles overlap.
# From (1,0) to (2,3), all three rectangles overlap.
# Example 2:

# Input: rectangles = [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 1018 modulo (109 + 7), which is 49.


# Constraints:

# 1 <= rectangles.length <= 200
# rectanges[i].length == 4
# 0 <= xi1, yi1, xi2, yi2 <= 109
# xi1 <= xi2
# yi1 <= yi2
# All rectangles have non zero area.
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
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        xs = sorted(set([r[0] for r in rectangles] + [r[2] for r in rectangles]))
        ys = sorted(set([r[1] for r in rectangles] + [r[3] for r in rectangles]))

        x_map = {x: i for i, x in enumerate(xs)}
        y_map = {y: i for i, y in enumerate(ys)}

        grid = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]

        for x1, y1, x2, y2 in rectangles:
            for i in range(x_map[x1], x_map[x2]):
                for j in range(y_map[y1], y_map[y2]):
                    grid[i][j] = True

        area = 0

        for i in range(len(xs) - 1):
            for j in range(len(ys) - 1):
                if grid[i][j]:
                    area += (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])

        return area % MOD







# Optimal:
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        ys = sorted(set(y for _, y1, _, y2 in rectangles for y in (y1, y2)))
        y_map = {y: i for i, y in enumerate(ys)}

        events = []

        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))
            events.append((x2, y1, y2, -1))

        events.sort()

        n = len(ys) - 1
        count = [0] * (4 * n)
        length = [0] * (4 * n)

        def update(node, left, right, ql, qr, value):
            if ql <= left and right <= qr:
                count[node] += value
            else:
                mid = (left + right) // 2

                if ql <= mid:
                    update(node * 2, left, mid, ql, qr, value)

                if qr > mid:
                    update(node * 2 + 1, mid + 1, right, ql, qr, value)

            if count[node] > 0:
                length[node] = ys[right + 1] - ys[left]
            elif left == right:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        area = 0
        prev_x = events[0][0]
        i = 0

        while i < len(events):
            x = events[i][0]

            area += (x - prev_x) * length[1]

            while i < len(events) and events[i][0] == x:
                _, y1, y2, value = events[i]
                update(
                    1,
                    0,
                    n - 1,
                    y_map[y1],
                    y_map[y2] - 1,
                    value
                )
                i += 1

            prev_x = x

        return area % MOD
