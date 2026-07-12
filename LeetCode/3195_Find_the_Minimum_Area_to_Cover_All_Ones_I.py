# You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.
# 
# Return the minimum possible area of the rectangle.
# 
# Example 1:
# Input: grid = [[0,1,0],[1,0,1]]
# Output: 6
# Explanation: The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.
# 
# Constraints:
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 0 or 1.
# The input is generated such that there is at least one 1 in grid.

# Brute Force Solution
class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        min_r, max_r = len(grid), -1
        min_c, max_c = len(grid[0]), -1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    min_r = min(min_r, r)
                    max_r = max(max_r, r)
                    min_c = min(min_c, c)
                    max_c = max(max_c, c)
                    
        return (max_r - min_r + 1) * (max_c - min_c + 1)

# Optimal Solution
class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        # The brute force is already O(N * M) which is optimal
        min_r, max_r = len(grid), -1
        min_c, max_c = len(grid[0]), -1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if r < min_r: min_r = r
                    if r > max_r: max_r = r
                    if c < min_c: min_c = c
                    if c > max_c: max_c = c
                    
        return (max_r - min_r + 1) * (max_c - min_c + 1)
