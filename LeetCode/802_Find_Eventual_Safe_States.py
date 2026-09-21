# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

# Example 1:

# Illustration of graph
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
# Example 2:

# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation:
# Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

# Constraints:

# n == graph.length
# 1 <= n <= 104
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 104].














# Brute Force - DFS

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            if state[node] == 3:
                return False

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    state[node] = 3
                    return False

            state[node] = 2
            return True

        result = []

        for i in range(n):
            if dfs(i):
                result.append(i)

        return result















# Optimal - Topological Sort

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)

        reverse = [[] for _ in range(n)]
        outdegree = [0] * n

        for i in range(n):
            outdegree[i] = len(graph[i])

            for nei in graph[i]:
                reverse[nei].append(i)

        q = deque()

        for i in range(n):
            if outdegree[i] == 0:
                q.append(i)

        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True

            for prev in reverse[node]:
                outdegree[prev] -= 1

                if outdegree[prev] == 0:
                    q.append(prev)

        return [i for i in range(n) if safe[i]]