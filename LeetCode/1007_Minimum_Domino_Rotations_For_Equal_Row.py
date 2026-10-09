# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.



# Example 1:


# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of values equal.


# Constraints:

# 2 <= tops.length <= 2 * 104
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6
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
# ### Brute Force — O(6n)

python
```

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        ans = float('inf')

        for target in range(1, 7):
            top_rot = 0
            bottom_rot = 0
            possible = True

            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    possible = False
                    break

                if tops[i] != target:
                    top_rot += 1

                if bottoms[i] != target:
                    bottom_rot += 1

            if possible:
                ans = min(ans, top_rot, bottom_rot)

        return ans if ans != float('inf') else -1
```

### Optimal — O(n) Time, O(1) Space

python
```

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def check(target):
            top_rot = 0
            bottom_rot = 0

            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return float('inf')

                if t != target:
                    top_rot += 1

                if b != target:
                    bottom_rot += 1

            return min(top_rot, bottom_rot)

        result = min(check(tops[0]), check(bottoms[0]))
        return result if result != float('inf') else -1
```
