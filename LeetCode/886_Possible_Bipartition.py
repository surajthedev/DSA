# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.



# Example 1:

# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: The first group has [1,4], and the second group has [2,3].
# Example 2:

# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.


# Constraints:

# 1 <= n <= 2000
# 0 <= dislikes.length <= 104
# dislikes[i].length == 2
# 1 <= ai < bi <= n
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
#
# # Brute Force - O(2^n * E)
class Solution:
    def possibleBipartition(self, n, dislikes):
        for mask in range(1 << n):
            valid = True

            for a, b in dislikes:
                a -= 1
                b -= 1

                if ((mask >> a) & 1) == ((mask >> b) & 1):
                    valid = False
                    break

            if valid:
                return True

        return False















# Optimal - O(n + E)
from collections import deque

class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = [[] for _ in range(n + 1)]

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (n + 1)

        for start in range(1, n + 1):
            if color[start] != 0:
                continue

            color[start] = 1
            q = deque([start])

            while q:
                u = q.popleft()

                for v in graph[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        q.append(v)

                    elif color[v] == color[u]:
                        return False

        return True
