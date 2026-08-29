# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.







# Brute force:
class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        # Outside grid OR water
                        if (
                            nr < 0 or nr >= rows or
                            nc < 0 or nc >= cols or
                            grid[nr][nc] == 0
                        ):
                            perimeter += 1

        return perimeter






# Optimal:
class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    # Every land cell has 4 sides
                    perimeter += 4

                    # Shared side with upper cell
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2

                    # Shared side with left cell
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2

        return perimeter