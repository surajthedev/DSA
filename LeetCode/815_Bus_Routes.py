# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1




# Constraints:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 105
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 105
# 0 <= routes[i][j] < 106
# 0 <= source, target < 106
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
from collections import deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        n = len(routes)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if set(routes[i]) & set(routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        start = []
        target_buses = set()

        for i in range(n):
            if source in routes[i]:
                start.append(i)
            if target in routes[i]:
                target_buses.add(i)

        q = deque()
        visited = set()

        for bus in start:
            q.append((bus, 1))
            visited.add(bus)

        while q:
            bus, count = q.popleft()

            if bus in target_buses:
                return count

            for nxt in graph[bus]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, count + 1))

        return -1











# Optimal:
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)

        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus)

        q = deque([(source, 0)])
        visited_stops = {source}
        visited_buses = set()

        while q:
            stop, buses_taken = q.popleft()

            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue

                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, buses_taken + 1))

        return -1
