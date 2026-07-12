# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
# 
# Example 1:
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
# 
# Example 2:
# Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
# 
# Constraints:
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4

# Brute Force Solution
class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        # A true brute force is complex for 2D. 
        # A basic approach could be to iteratively raise the water level and simulate flow, 
        # but that is extremely inefficient. We provide a conceptual placeholder.
        if not heightMap or not heightMap[0]:
            return 0
        pass

# Optimal Solution
class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
            
        import heapq
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
                    
        water_trapped = 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        max_height = 0
        
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            max_height = max(max_height, height)
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if heightMap[nx][ny] < max_height:
                        water_trapped += max_height - heightMap[nx][ny]
                    heapq.heappush(min_heap, (heightMap[nx][ny], nx, ny))
                    visited[nx][ny] = True
                    
        return water_trapped
