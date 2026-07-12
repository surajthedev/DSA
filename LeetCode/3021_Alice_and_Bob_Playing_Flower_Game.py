# Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The circle represents the field, and there are x flowers in the clockwise direction between Alice and Bob, and y flowers in the anti-clockwise direction between them.
# 
# The game proceeds as follows:
# 1. Alice takes the first turn.
# 2. In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one flower from that direction.
# 3. At the end of a player's turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
# 
# Given two integers, n and m, the number of flowers x and y are randomly chosen such that 1 <= x <= n and 1 <= y <= m.
# Return the total number of pairs (x, y) that satisfy the conditions where Alice will win if both players play optimally.
# 
# Example 1:
# Input: n = 3, m = 2
# Output: 3
# Explanation: The following pairs satisfy conditions: (1,2), (3,2), (2,1).
# 
# Example 2:
# Input: n = 1, m = 1
# Output: 0
# Explanation: No pairs satisfy the conditions.
# 
# Constraints:
# 1 <= n, m <= 10^5

# Brute Force Solution
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        count = 0
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if (x + y) % 2 == 1:
                    count += 1
        return count

# Optimal Solution
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Alice wins if (x + y) is odd
        # We need to pick one odd from n and one even from m
        # OR one even from n and one odd from m
        
        odd_n = (n + 1) // 2
        even_n = n // 2
        
        odd_m = (m + 1) // 2
        even_m = m // 2
        
        return odd_n * even_m + even_n * odd_m
