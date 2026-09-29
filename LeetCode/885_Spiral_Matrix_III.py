# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

# Return an array of coordinates representing the positions of the grid in the order you visited them.



# Example 1:


# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
# Example 2:


# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


# Constraints:

# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols
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
#
# # Brute Force
class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        visited = set()
        ans = []

        r, c = rStart, cStart
        visited.add((r, c))
        ans.append([r, c])

        while len(ans) < rows * cols:
            # Move east
            for _ in range(1):
                c += 1
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    ans.append([r, c])

            # Move south
            for _ in range(1):
                r += 1
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    ans.append([r, c])

            # Move west
            for _ in range(2):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    ans.append([r, c])

            # Move north
            for _ in range(2):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    ans.append([r, c])

            # Increase spiral size
            for _ in range(3):
                c += 1
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    ans.append([r, c])

            for _ in range(3):
                r += 1
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    ans.append([r, c])

            # Continue with generic spiral from here
            step = 4
            while len(ans) < rows * cols:
                for _ in range(step):
                    c -= 1
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        visited.add((r, c))
                        ans.append([r, c])

                for _ in range(step):
                    r -= 1
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        visited.add((r, c))
                        ans.append([r, c])

                step += 1

                for _ in range(step):
                    c += 1
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        visited.add((r, c))
                        ans.append([r, c])

                for _ in range(step):
                    r += 1
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        visited.add((r, c))
                        ans.append([r, c])

                step += 1

        return ans















# Optimal - O(rows * cols) Time, O(1) extra space
class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        ans = []

        r, c = rStart, cStart
        ans.append([r, c])

        step = 1

        while len(ans) < rows * cols:
            # East
            for _ in range(step):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])

            # South
            for _ in range(step):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])

            step += 1

            # West
            for _ in range(step):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])

            # North
            for _ in range(step):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])

            step += 1

        return ans
