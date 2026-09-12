# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.








# Brute force: 
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        def has_cycle(u, v, graph):
            visited = [False] * (n + 1)

            def dfs(node, parent):
                visited[node] = True

                for nei in graph[node]:
                    if nei == parent:
                        continue

                    if visited[nei] or dfs(nei, node):
                        return True

                return False

            return dfs(u, -1)

        answer = []

        for u, v in edges:
            graph = [[] for _ in range(n + 1)]

            for a, b in edges:
                if [a, b] == [u, v]:
                    continue

                graph[a].append(b)
                graph[b].append(a)

            if has_cycle(u, v, graph):
                answer = [u, v]

        return answer








# Optimal:
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False

            if rank[ra] < rank[rb]:
                ra, rb = rb, ra

            parent[rb] = ra

            if rank[ra] == rank[rb]:
                rank[ra] += 1

            return True

        answer = []

        for u, v in edges:
            if not union(u, v):
                answer = [u, v]

        return answer