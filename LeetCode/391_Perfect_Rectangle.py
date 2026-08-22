# Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

# Return true if all the rectangles together form an exact cover of a rectangular region.

 

# Example 1:


# Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
# Output: true
# Explanation: All 5 rectangles together form an exact cover of a rectangular region.
# Example 2:


# Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
# Output: false
# Explanation: Because there is a gap between the two rectangular regions.
# Example 3:


# Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
# Output: false
# Explanation: Because two of the rectangles overlap with each other.
 

# Constraints:

# 1 <= rectangles.length <= 2 * 104
# rectangles[i].length == 4
# -105 <= xi < ai <= 105
# -105 <= yi < bi <= 105



# Brute force:
class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:

        n = len(rectangles)

        # Check every pair for overlap
        for i in range(n):
            x1, y1, a1, b1 = rectangles[i]

            for j in range(i + 1, n):
                x2, y2, a2, b2 = rectangles[j]

                # Check if rectangles overlap
                if x1 < a2 and x2 < a1 and y1 < b2 and y2 < b1:
                    return False

        # Find bounding rectangle
        min_x = min(rect[0] for rect in rectangles)
        min_y = min(rect[1] for rect in rectangles)
        max_x = max(rect[2] for rect in rectangles)
        max_y = max(rect[3] for rect in rectangles)

        # Calculate total area of small rectangles
        total_area = 0

        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)

        # Area of bounding rectangle
        bounding_area = (max_x - min_x) * (max_y - min_y)

        return total_area == bounding_area






# Optimal:
class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:

        corners = set()

        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')

        total_area = 0

        for x1, y1, x2, y2 in rectangles:

            # Update bounding rectangle
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Add area
            total_area += (x2 - x1) * (y2 - y1)

            # Four corners
            points = [
                (x1, y1),
                (x1, y2),
                (x2, y1),
                (x2, y2)
            ]

            # Toggle corners
            for point in points:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)

        # Bounding rectangle area
        bounding_area = (max_x - min_x) * (max_y - min_y)

        # Must have exactly 4 outer corners
        if len(corners) != 4:
            return False

        # Check that the 4 remaining corners
        # are exactly the bounding rectangle corners
        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        return total_area == bounding_area and corners == expected_corners