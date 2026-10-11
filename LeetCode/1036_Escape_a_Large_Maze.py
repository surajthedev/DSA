# There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).

# We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).

# Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. We are also not allowed to walk outside of the grid.

# Return true if and only if it is possible to reach the target square from the source square through a sequence of valid moves.



# Example 1:

# Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# Output: false
# Explanation: The target square is inaccessible starting from the source square because we cannot move.
# We cannot move north or east because those squares are blocked.
# We cannot move south or west because we cannot go outside of the grid.
# Example 2:

# Input: blocked = [], source = [0,0], target = [999999,999999]
# Output: true
# Explanation: Because there are no blocked cells, it is possible to reach the target square.


# Constraints:

# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= xi, yi < 106
# source.length == target.length == 2
# 0 <= sx, sy, tx, ty < 106
# source != target
# It is guaranteed that source and target are not blocked.
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
# ### Brute Force (BFS — Not Practical for Full Grid)

python
```
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        blocked = {tuple(cell) for cell in blocked}
        LIMIT = 10**6
        queue = deque([tuple(source)])
        visited = {tuple(source)}

        while queue:
            x, y = queue.popleft()

            if [x, y] == target:
                return True

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if (0 <= nx < LIMIT and 0 <= ny < LIMIT
                        and (nx, ny) not in blocked
                        and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False
```

### Optimal (BFS with Blocking Bound)

python
```
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        blocked = {tuple(cell) for cell in blocked}
        LIMIT = 10**6
        max_area = len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            queue = deque([tuple(start)])
            visited = {tuple(start)}

            while queue:
                x, y = queue.popleft()

                if (x, y) == tuple(end) or len(visited) > max_area:
                    return True

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < LIMIT and 0 <= ny < LIMIT
                            and (nx, ny) not in blocked
                            and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        queue.append((nx, ny))

            return False

        return bfs(source, target) and bfs(target, source)
```
