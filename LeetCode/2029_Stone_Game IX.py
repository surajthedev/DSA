# Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.

# Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

# Assuming both players play optimally, return true if Alice wins and false if Bob wins.

 

# Example 1:

# Input: stones = [2,1]
# Output: true
# Explanation: The game will be played as follows:
# - Turn 1: Alice can remove either stone.
# - Turn 2: Bob removes the remaining stone. 
# The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
# Example 2:

# Input: stones = [2]
# Output: false
# Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
# Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
# Example 3:

# Input: stones = [5,1,2,4,3]
# Output: false
# Explanation: Bob will always win. One possible way for Bob to win is shown below:
# - Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
# - Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
# - Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
# - Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
# - Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
# Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.
 

# Constraints:

# 1 <= stones.length <= 105
# 1 <= stones[i] <= 104






# Brute force:
from functools import lru_cache


def alice_wins_bruteforce(stones):
    n = len(stones)

    @lru_cache(None)
    def dp(mask, current_sum, turn):
        # turn = 0 -> Alice
        # turn = 1 -> Bob

        # No stones left -> Bob wins automatically
        if mask == 0:
            return False

        results = []

        for i in range(n):
            if mask & (1 << i):
                new_sum = (current_sum + stones[i]) % 3

                # This move makes sum divisible by 3.
                # Current player loses immediately.
                if new_sum == 0:
                    result = False if turn == 0 else True

                else:
                    result = dp(
                        mask ^ (1 << i),
                        new_sum,
                        1 - turn
                    )

                results.append(result)

        if turn == 0:
            # Alice chooses a move that makes Alice win
            return any(results)
        else:
            # Bob will choose a move that makes Alice lose
            return all(results)

    return dp((1 << n) - 1, 0, 0)







# Optimal:
class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        zero, one, two = cnt

        # Number of 0-mod-3 stones is even
        if zero % 2 == 0:
            return one > 0 and two > 0

        # Number of 0-mod-3 stones is odd
        return abs(one - two) >= 3