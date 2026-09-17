# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 

# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
 






# Brute force:
class Solution:
    def networkDelayTime(self, times, n, k):
        INF = float("inf")
        dist = [INF] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1):
            updated = False

            for u, v, w in times:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

            if not updated:
                break

        ans = max(dist[1:])

        return -1 if ans == INF else ans











# Optimal:
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            time, u = heapq.heappop(heap)

            if time > dist[u]:
                continue

            for v, w in graph[u]:
                new_time = time + w

                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(heap, (new_time, v))

        ans = max(dist[1:])

        return -1 if ans == float("inf") else ans