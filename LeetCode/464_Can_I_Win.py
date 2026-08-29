# In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

# What if we change the game so that players cannot re-use integers?

# For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

# Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

 

# Example 1:

# Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.
# Example 2:

# Input: maxChoosableInteger = 10, desiredTotal = 0
# Output: true
# Example 3:

# Input: maxChoosableInteger = 10, desiredTotal = 1
# Output: true
 

# Constraints:

# 1 <= maxChoosableInteger <= 20
# 0 <= desiredTotal <= 300






# Brute force:
class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):

        def dfs(remaining, used):
            # Try every available number
            for num in range(1, maxChoosableInteger + 1):

                if used[num]:
                    continue

                # If choosing num wins immediately
                if num >= remaining:
                    return True

                # Choose num
                used[num] = True

                # If opponent cannot win, current player wins
                if not dfs(remaining - num, used):
                    used[num] = False
                    return True

                # Undo choice
                used[num] = False

            # No move can guarantee a win
            return False

        return dfs(desiredTotal, [False] * (maxChoosableInteger + 1))







# Optimal:
class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):

        # Case 1:
        # First player can immediately win
        if desiredTotal <= 0:
            return True

        # Maximum sum possible using every number
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        # Even after using every number, target cannot be reached
        if total_sum < desiredTotal:
            return False

        memo = {}

        def dfs(mask, remaining):

            # Already computed this state
            if mask in memo:
                return memo[mask]

            # Try every number
            for num in range(1, maxChoosableInteger + 1):

                # Check whether num is already used
                if mask & (1 << num):
                    continue

                # If this number reaches the target,
                # current player wins immediately.
                if num >= remaining:
                    memo[mask] = True
                    return True

                # Choose num
                new_mask = mask | (1 << num)

                # If opponent loses from this state,
                # current player can force a win.
                if not dfs(new_mask, remaining - num):
                    memo[mask] = True
                    return True

            # No winning move found
            memo[mask] = False
            return False

        return dfs(0, desiredTotal)