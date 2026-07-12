# You are given a 2D integer matrix grid of size n x m.
# 
# Return the length of the longest V-shaped diagonal segment in grid.
# 
# Constraints:
# 1 <= n, m <= 500
# grid[i][j] is either 0, 1, or 2.

# Brute Force Solution
class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_len = 0
        
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < m
            
        def getLen(r, c, d_idx, turn_allowed, current_val):
            dr, dc = dirs[d_idx]
            nr, nc = r + dr, c + dc
            if not isValid(nr, nc):
                return 0
                
            next_expected = 2 if current_val == 1 else 1
            if grid[nr][nc] != next_expected:
                return 0
                
            ans = 1 + getLen(nr, nc, d_idx, turn_allowed, next_expected)
            
            if turn_allowed:
                next_d_idx = (d_idx + 1) % 4
                ans = max(ans, 1 + getLen(nr, nc, next_d_idx, False, next_expected))
                
            return ans

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d_idx in range(4):
                        max_len = max(max_len, 1 + getLen(i, j, d_idx, True, 1))
                        
        return max_len if max_len > 0 else (1 if any(1 in row for row in grid) else 0)

# Optimal Solution
class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        from functools import lru_cache
        
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        
        @lru_cache(None)
        def dfs(r, c, d_idx, turned, val):
            dr, dc = dirs[d_idx]
            nr, nc = r + dr, c + dc
            
            if not (0 <= nr < n and 0 <= nc < m):
                return 0
                
            expected = 2 if val == 1 else 1
            if grid[nr][nc] != expected:
                return 0
                
            res = 1 + dfs(nr, nc, d_idx, turned, expected)
            if not turned:
                next_d = (d_idx + 1) % 4
                res = max(res, 1 + dfs(nr, nc, next_d, True, expected))
                
            return res

        ans = 0
        has_one = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    has_one = True
                    for d in range(4):
                        ans = max(ans, 1 + dfs(i, j, d, False, 1))
                        
        return ans if ans > 0 else (1 if has_one else 0)
