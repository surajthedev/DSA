# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

# Choosing any integer x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.

# Return true if and only if Alice wins the game, assuming both players play optimally.



# Example 1:

# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# Example 2:

# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.


# Constraints:

# 1 <= n <= 1000
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
# ### Brute Force — Recursion + Memoization

python
```

from functools import lru_cache

class Solution:
    def divisorGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(num):
            for x in range(1, num):
                if num % x == 0:
                    if not dfs(num - x):
                        return True
            return False

        return dfs(n)
```

### Optimal — Math

python
```

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
```
