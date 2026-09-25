# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.



# Example 1:


# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# Example 2:


# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]


# Constraints:

# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] does not contain i.
# If graph[a] contains b, then graph[b] contains a.
# The input graph is always connected.
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
# Brute force:
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        full = (1 << n) - 1
        ans = float('inf')

        def dfs(node, mask, dist, visited):
            nonlocal ans

            if mask == full:
                ans = min(ans, dist)
                return

            if dist >= ans:
                return

            state = (node, mask)

            if state in visited and visited[state] <= dist:
                return

            visited[state] = dist

            for nei in graph[node]:
                dfs(
                    nei,
                    mask | (1 << nei),
                    dist + 1,
                    visited
                )

        for start in range(n):
            dfs(start, 1 << start, 0, {})

        return ans








# Optimal:
from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        full = (1 << n) - 1

        queue = deque()
        visited = set()

        # Start BFS from every node
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))

        while queue:
            node, mask, dist = queue.popleft()

            if mask == full:
                return dist

            for nei in graph[node]:
                new_mask = mask | (1 << nei)
                state = (nei, new_mask)

                if state not in visited:
                    visited.add(state)
                    queue.append((nei, new_mask, dist + 1))

        return 0
