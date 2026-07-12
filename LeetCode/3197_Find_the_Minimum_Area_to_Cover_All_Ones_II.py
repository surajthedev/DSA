# You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.
# 
# Return the minimum possible sum of the area of these rectangles.
# 
# Constraints:
# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] is either 0 or 1.
# The input is generated such that there are at least three 1's in grid.

# Brute Force Solution
class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:
        def get_area(r1, r2, c1, c2):
            min_r, max_r = 100, -1
            min_c, max_c = 100, -1
            has_one = False
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        has_one = True
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
            if not has_one: return 0
            return (max_r - min_r + 1) * (max_c - min_c + 1)
            
        m, n = len(grid), len(grid[0])
        res = float('inf')
        
        # 6 possible ways to split grid into 3 rectangles
        # 1. 2 horizontal cuts
        for i in range(m - 2):
            for j in range(i + 1, m - 1):
                a1 = get_area(0, i, 0, n - 1)
                a2 = get_area(i + 1, j, 0, n - 1)
                a3 = get_area(j + 1, m - 1, 0, n - 1)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        # 2. 2 vertical cuts
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                a1 = get_area(0, m - 1, 0, i)
                a2 = get_area(0, m - 1, i + 1, j)
                a3 = get_area(0, m - 1, j + 1, n - 1)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        # 3. 1 horz, then bottom has 1 vert cut
        for i in range(m - 1):
            for j in range(n - 1):
                a1 = get_area(0, i, 0, n - 1)
                a2 = get_area(i + 1, m - 1, 0, j)
                a3 = get_area(i + 1, m - 1, j + 1, n - 1)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        # 4. 1 horz, then top has 1 vert cut
        for i in range(m - 1):
            for j in range(n - 1):
                a1 = get_area(i + 1, m - 1, 0, n - 1)
                a2 = get_area(0, i, 0, j)
                a3 = get_area(0, i, j + 1, n - 1)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        # 5. 1 vert, then right has 1 horz cut
        for j in range(n - 1):
            for i in range(m - 1):
                a1 = get_area(0, m - 1, 0, j)
                a2 = get_area(0, i, j + 1, n - 1)
                a3 = get_area(i + 1, m - 1, j + 1, n - 1)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        # 6. 1 vert, then left has 1 horz cut
        for j in range(n - 1):
            for i in range(m - 1):
                a1 = get_area(0, m - 1, j + 1, n - 1)
                a2 = get_area(0, i, 0, j)
                a3 = get_area(i + 1, m - 1, 0, j)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        return res

# Optimal Solution
class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:
        # Same as brute force since constraints are very small (<=30)
        def get_area(r1, r2, c1, c2):
            min_r, max_r = 100, -1
            min_c, max_c = 100, -1
            has_one = False
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        has_one = True
                        if r < min_r: min_r = r
                        if r > max_r: max_r = r
                        if c < min_c: min_c = c
                        if c > max_c: max_c = c
            if not has_one: return 0
            return (max_r - min_r + 1) * (max_c - min_c + 1)
            
        m, n = len(grid), len(grid[0])
        res = float('inf')
        
        # Checking all 6 layouts
        for i in range(m - 1):
            for j in range(i + 1, m - 1):
                a1 = get_area(0, i, 0, n - 1)
                a2 = get_area(i + 1, j, 0, n - 1)
                a3 = get_area(j + 1, m - 1, 0, n - 1)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                a1 = get_area(0, m - 1, 0, i)
                a2 = get_area(0, m - 1, i + 1, j)
                a3 = get_area(0, m - 1, j + 1, n - 1)
                if a1 and a2 and a3: res = min(res, a1 + a2 + a3)
                
        for i in range(m - 1):
            for j in range(n - 1):
                res = min(res, get_area(0, i, 0, n - 1) + get_area(i + 1, m - 1, 0, j) + get_area(i + 1, m - 1, j + 1, n - 1))
                res = min(res, get_area(i + 1, m - 1, 0, n - 1) + get_area(0, i, 0, j) + get_area(0, i, j + 1, n - 1))
                
        for j in range(n - 1):
            for i in range(m - 1):
                res = min(res, get_area(0, m - 1, 0, j) + get_area(0, i, j + 1, n - 1) + get_area(i + 1, m - 1, j + 1, n - 1))
                res = min(res, get_area(0, m - 1, j + 1, n - 1) + get_area(0, i, 0, j) + get_area(i + 1, m - 1, 0, j))
                
        return res
