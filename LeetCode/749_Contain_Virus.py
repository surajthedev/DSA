# A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

# The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

# Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.

# Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.

 

# Example 1:


# Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
# Output: 10
# Explanation: There are 2 contaminated regions.
# On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

# On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

# Example 2:


# Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 4
# Explanation: Even though there is only one cell saved, there are 4 walls built.
# Notice that walls are only built on the shared boundary of two different cells.
# Example 3:

# Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
# Output: 13
# Explanation: The region on the left only builds two new walls.
 

# Constraints:

# m == isInfected.length
# n == isInfected[i].length
# 1 <= m, n <= 50
# isInfected[i][j] is either 0 or 1.
# There is always a contiguous viral region throughout the described process that will infect strictly more uncontaminated squares in the next round.








# Brute force:
class Solution:
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        walls = 0

        while True:
            regions = []
            frontiers = []
            wall_counts = []

            visited = [[False] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        stack = [(i, j)]
                        visited[i][j] = True
                        region = []
                        frontier = set()
                        wall_count = 0

                        while stack:
                            r, c = stack.pop()
                            region.append((r, c))

                            for dr, dc in dirs:
                                nr, nc = r + dr, c + dc

                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 1 and not visited[nr][nc]:
                                        visited[nr][nc] = True
                                        stack.append((nr, nc))

                                    elif isInfected[nr][nc] == 0:
                                        frontier.add((nr, nc))
                                        wall_count += 1

                        regions.append(region)
                        frontiers.append(frontier)
                        wall_counts.append(wall_count)

            if not regions:
                break

            idx = max(range(len(regions)), key=lambda x: len(frontiers[x]))

            if not frontiers[idx]:
                break

            walls += wall_counts[idx]

            for r, c in regions[idx]:
                isInfected[r][c] = -1

            for i in range(len(regions)):
                if i == idx:
                    continue

                for r, c in frontiers[i]:
                    isInfected[r][c] = 1

        return walls












# Optimal:
class Solution:
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0

        while True:
            regions = []
            frontiers = []
            walls = []

            visited = [[False] * n for _ in range(m)]

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and not visited[r][c]:

                        region = []
                        frontier = set()
                        wall_count = 0
                        stack = [(r, c)]
                        visited[r][c] = True

                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))

                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy

                                if not (0 <= nx < m and 0 <= ny < n):
                                    continue

                                if isInfected[nx][ny] == 1:
                                    if not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        stack.append((nx, ny))

                                elif isInfected[nx][ny] == 0:
                                    frontier.add((nx, ny))
                                    wall_count += 1

                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall_count)

            if not regions:
                break

            quarantine = max(
                range(len(frontiers)),
                key=lambda i: len(frontiers[i])
            )

            if len(frontiers[quarantine]) == 0:
                break

            ans += walls[quarantine]

            for r, c in regions[quarantine]:
                isInfected[r][c] = -1

            for i in range(len(frontiers)):
                if i == quarantine:
                    continue

                for r, c in frontiers[i]:
                    isInfected[r][c] = 1

        return ans