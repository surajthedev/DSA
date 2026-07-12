# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
# 
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
# 
# A connected component is said to be complete if there exists an edge between every pair of its vertices.
# 
# Return the number of complete connected components in the given graph.
# 
# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components are complete.
# 
# Example 2:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
# 
# Constraints:
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated edges.

# Brute Force Solution
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        from collections import defaultdict
        
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        visited = set()
        count = 0
        
        for i in range(n):
            if i not in visited:
                comp_nodes = []
                q = [i]
                visited.add(i)
                while q:
                    curr = q.pop(0)
                    comp_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            
                # Check if complete
                is_complete = True
                for node in comp_nodes:
                    if len(adj[node]) != len(comp_nodes) - 1:
                        is_complete = False
                        break
                        
                if is_complete:
                    count += 1
                    
        return count

# Optimal Solution
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        res = 0
        
        for i in range(n):
            if not visited[i]:
                nodes_count = 0
                edges_count = 0
                
                def dfs(node):
                    nonlocal nodes_count, edges_count
                    visited[node] = True
                    nodes_count += 1
                    edges_count += len(adj[node])
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            dfs(neighbor)
                            
                dfs(i)
                
                # In an undirected graph, total edges in component = edges_count / 2
                # A complete graph has n*(n-1)/2 edges
                if edges_count == nodes_count * (nodes_count - 1):
                    res += 1
                    
        return res
