# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.



# Example 1:

# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
# Example 2:

# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
# Example 3:

# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.


# Constraints:

# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 104
# No two stones are at the same coordinate point.
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
# Brute force:
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [False] * n

        def dfs(i):
            visited[i] = True

            for j in range(n):
                if not visited[j]:
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                        dfs(j)

        components = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return n - components













# Optimal:
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for x, y in stones:
            row = x
            col = ~y

            if row not in parent:
                parent[row] = row

            if col not in parent:
                parent[col] = col

            union(row, col)

        components = len({find(x) for x in parent})

        return len(stones) - components
