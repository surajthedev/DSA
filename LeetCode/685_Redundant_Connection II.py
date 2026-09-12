# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

# The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

# Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# Output: [4,1]
 

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi








# Brute force: 
class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)

        def valid(skip):
            parent = [0] * (n + 1)
            graph = [[] for _ in range(n + 1)]

            for i, (u, v) in enumerate(edges):
                if i == skip:
                    continue

                if parent[v] != 0:
                    return False

                parent[v] = u
                graph[u].append(v)

            root = 0
            for i in range(1, n + 1):
                if parent[i] == 0:
                    if root != 0:
                        return False
                    root = i

            visited = [False] * (n + 1)

            def dfs(node):
                if visited[node]:
                    return False

                visited[node] = True

                for nei in graph[node]:
                    if not dfs(nei):
                        return False

                return True

            return dfs(root) and all(visited[1:])

        for i in range(n - 1, -1, -1):
            if valid(i):
                return edges[i]

        return []







# Optimal:
class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = [0] * (n + 1)

        candidate1 = None
        candidate2 = None

        # Find a node with two parents
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]

        # Union Find
        uf = list(range(n + 1))

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False

            uf[rb] = ra
            return True

        # If a node has two parents, skip the later candidate first
        for edge in edges:
            if candidate2 and edge == candidate2:
                continue

            if not union(edge[0], edge[1]):
                if candidate1:
                    return candidate1
                return edge

        return candidate2