# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Return the knight's minimum initial health so that he can rescue the princess.

# Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

# Example 1:


# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7
# Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
# Example 2:

# Input: dungeon = [[0]]
# Output: 1
 

# Constraints:

# m == dungeon.length
# n == dungeon[i].length
# 1 <= m, n <= 200
# -1000 <= dungeon[i][j] <= 1000






# Brute force:
class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        def dfs(i, j):
            # Last cell
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])

            right = float('inf')
            down = float('inf')

            if j + 1 < n:
                right = dfs(i, j + 1)

            if i + 1 < m:
                down = dfs(i + 1, j)

            # Choose the path requiring less initial health
            needed_after = min(right, down)

            return max(1, needed_after - dungeon[i][j])

        return dfs(0, 0)









# Optimal:
class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [float('inf')] * (n + 1)
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                needed = min(dp[j], dp[j + 1])

                dp[j] = max(
                    1,
                    needed - dungeon[i][j]
                )

        return dp[0]