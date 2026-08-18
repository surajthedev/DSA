# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

# Example 1:


# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# Example 2:


# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

# Constraints:

# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi





# Brute force:
class Solution:
    def findItinerary(self, tickets):
        n = len(tickets)
        used = [False] * n
        path = ["JFK"]
        answer = None

        def backtrack(current):
            nonlocal answer

            if len(path) == n + 1:
                candidate = path[:]

                if answer is None or candidate < answer:
                    answer = candidate

                return

            for i in range(n):
                if not used[i] and tickets[i][0] == current:
                    used[i] = True
                    path.append(tickets[i][1])

                    backtrack(tickets[i][1])

                    path.pop()
                    used[i] = False

        backtrack("JFK")

        return answer







# Optimal:
class Solution:
    def findItinerary(self, tickets):
        graph = {}

        for src, dst in tickets:
            if src not in graph:
                graph[src] = []

            graph[src].append(dst)

        # Reverse sort so we can pop smallest destination
        for src in graph:
            graph[src].sort(reverse=True)

        result = []

        def dfs(airport):
            while graph.get(airport):
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]