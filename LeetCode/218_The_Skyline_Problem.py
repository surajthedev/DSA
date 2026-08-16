# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

# The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

# lefti is the x coordinate of the left edge of the ith building.
# righti is the x coordinate of the right edge of the ith building.
# heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

# Example 1:


# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
# Example 2:

# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
 

# Constraints:

# 1 <= buildings.length <= 104
# 0 <= lefti < righti <= 231 - 1
# 1 <= heighti <= 231 - 1
# buildings is sorted by lefti in non-decreasing order.





# Brute force:
class Solution:
    def getSkyline(self, buildings):
        result = []

        # All important x coordinates
        xs = set()

        for left, right, height in buildings:
            xs.add(left)
            xs.add(right)

        xs = sorted(xs)

        for x in xs:
            max_height = 0

            # Check every building
            for left, right, height in buildings:
                if left <= x < right:
                    max_height = max(max_height, height)

            # Height change detect karna
            if not result or result[-1][1] != max_height:
                result.append([x, max_height])

        return result







# Optimal:
import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []

        # Create start and end events
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        # Sort events
        events.sort()

        result = []

        # (negative height, end)
        heap = [(0, float('inf'))]

        i = 0

        while i < len(events):
            x = events[i][0]

            # Process all events at same x
            while i < len(events) and events[i][0] == x:
                _, neg_height, right = events[i]

                if neg_height != 0:
                    heapq.heappush(heap, (neg_height, right))

                i += 1

            # Remove buildings which ended before/current x
            while heap[0][1] <= x:
                heapq.heappop(heap)

            current_height = -heap[0][0]

            # Height changed
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result