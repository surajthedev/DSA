# You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

# The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

# To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].

# In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

# Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.



# Example 1:


# Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
# Output: 13
# Explanation: The edge subdivisions are shown in the image above.
# The nodes that are reachable are highlighted in yellow.
# Example 2:

# Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
# Output: 23
# Example 3:

# Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
# Output: 1
# Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.


# Constraints:

# 0 <= edges.length <= min(n * (n - 1) / 2, 104)
# edges[i].length == 3
# 0 <= ui < vi < n
# There are no multiple edges in the graph.
# 0 <= cnti <= 104
# 0 <= maxMoves <= 109
# 1 <= n <= 3000
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
# # Brute Force - Explicitly build the subdivided graph
# Time: O(V + E + S), Space: O(V + E + S)
# S = total number of subdivided nodes

from collections import deque

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = [[] for _ in range(n)]

        next_node = n

        for u, v, cnt in edges:
            prev = u

            for _ in range(cnt):
                graph[prev].append(next_node)
                graph[next_node].append(prev)
                prev = next_node
                next_node += 1

            graph[prev].append(v)
            graph[v].append(prev)

        dist = [-1] * next_node
        dist[0] = 0

        q = deque([0])
        ans = 0

        while q:
            u = q.popleft()

            if dist[u] > maxMoves:
                continue

            ans += 1

            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if dist[v] <= maxMoves:
                        q.append(v)

        return ans















# Optimal - Dijkstra on original graph
# Time: O((n + E) log n)
# Space: O(n + E)

import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = [[] for _ in range(n)]

        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)

            if d != dist[u]:
                continue

            for v, cnt in graph[u]:
                nd = d + cnt + 1

                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        ans = sum(d <= maxMoves for d in dist)

        for u, v, cnt in edges:
            from_u = max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
            from_v = max(0, maxMoves - dist[v]) if dist[v] <= maxMoves else 0

            ans += min(cnt, from_u + from_v)

        return ans
