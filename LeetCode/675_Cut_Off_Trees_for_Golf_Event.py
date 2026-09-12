# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
# In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

# Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

 

# Example 1:


# Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
# Output: 6
# Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
# Example 2:


# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
# Example 3:

# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# Explanation: You can follow the same path as Example 1 to cut off all the trees.
# Note that you can cut off the first tree at (0, 0) before making any steps.
 

# Constraints:

# m == forest.length
# n == forest[i].length
# 1 <= m, n <= 50
# 0 <= forest[i][j] <= 109
# Heights of all trees are distinct.









# Brute force:
from collections import deque

class Solution:
    def cutOffTree(self, forest):
        m, n = len(forest), len(forest[0])

        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))

        trees.sort()

        def bfs(sr, sc, tr, tc):
            q = deque([(sr, sc, 0)])
            visited = {(sr, sc)}

            while q:
                r, c, d = q.popleft()

                if r == tr and c == tc:
                    return d

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n and
                        forest[nr][nc] != 0 and
                        (nr, nc) not in visited):

                        visited.add((nr, nc))
                        q.append((nr, nc, d + 1))

            return -1

        ans = 0
        r = c = 0

        for _, tr, tc in trees:
            dist = bfs(r, c, tr, tc)

            if dist == -1:
                return -1

            ans += dist
            r, c = tr, tc

        return ans








# Optimal:
from collections import deque

class Solution:
    def cutOffTree(self, forest):
        m, n = len(forest), len(forest[0])

        trees = sorted(
            (forest[r][c], r, c)
            for r in range(m)
            for c in range(n)
            if forest[r][c] > 1
        )

        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0

            q = deque([(sr, sc)])
            visited = {(sr, sc)}
            steps = 0

            while q:
                steps += 1

                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc

                        if (nr, nc) == (tr, tc):
                            return steps

                        if (0 <= nr < m and 0 <= nc < n and
                            forest[nr][nc] != 0 and
                            (nr, nc) not in visited):

                            visited.add((nr, nc))
                            q.append((nr, nc))

            return -1

        ans = 0
        sr = sc = 0

        for _, tr, tc in trees:
            dist = bfs(sr, sc, tr, tc)

            if dist == -1:
                return -1

            ans += dist
            sr, sc = tr, tc

        return ans