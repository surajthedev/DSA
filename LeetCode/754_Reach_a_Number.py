# You are standing at position 0 on an infinite number line. There is a destination at position target.

# You can make some number of moves numMoves so that:

# On each move, you can either go left or right.
# During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
# Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.

 

# Example 1:

# Input: target = 2
# Output: 3
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to -1 (2 steps).
# On the 3rd move, we step from -1 to 2 (3 steps).
# Example 2:

# Input: target = 3
# Output: 2
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to 3 (2 steps).
 

# Constraints:

# -109 <= target <= 109
# target != 0










# Brute Force

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        def dfs(move, position):
            if position == target:
                return move - 1

            if move > 50000:
                return float('inf')

            return min(
                dfs(move + 1, position + move),
                dfs(move + 1, position - move)
            )

        return dfs(1, 0)










# Optimal:

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        total = 0
        moves = 0

        while total < target or (total - target) % 2 != 0:
            moves += 1
            total += moves

        return moves