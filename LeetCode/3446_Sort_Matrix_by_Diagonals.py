# You are given an n x n integer matrix grid.
# 
# Sort the matrix such that each diagonal starting from the top row and left column is sorted in ascending order.
# 
# Example 1:
# Input: grid = [[1,7,3],[9,8,2],[4,5,6]]
# Output: [[1,2,3],[4,5,6],[7,8,9]]
# 
# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 100
# 1 <= grid[i][j] <= 10^5

# Brute Force Solution
class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        from collections import defaultdict
        
        diagonals = defaultdict(list)
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
                
        for key in diagonals:
            # Bottom-left diagonals (i-j > 0) descending, Top-right (i-j <= 0) ascending
            if key > 0:
                diagonals[key].sort(reverse=True)
            else:
                diagonals[key].sort()
                
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)
                
        return grid

# Optimal Solution
class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        from collections import defaultdict
        
        diagonals = defaultdict(list)
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
                
        for key in diagonals:
            if key > 0:
                diagonals[key].sort(reverse=True)
            else:
                diagonals[key].sort()
                
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)
                
        return grid
