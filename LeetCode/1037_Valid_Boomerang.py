# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

# A boomerang is a set of three points that are all distinct and not in a straight line.



# Example 1:

# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
# Example 2:

# Input: points = [[1,1],[2,2],[3,3]]
# Output: false


# Constraints:

# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100
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
#
#
#
# ### Brute Force

python
```
class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        p1, p2, p3 = points

        if p1 == p2 or p2 == p3 or p1 == p3:
            return False

        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        slope1 = (y2 - y1) * (x3 - x2)
        slope2 = (y3 - y2) * (x2 - x1)

        return slope1 != slope2
```

### Optimal (Cross Product)

python
```
class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points

        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
```
