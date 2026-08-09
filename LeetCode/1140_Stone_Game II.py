# Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

# Alice and Bob take turns, with Alice starting first.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

# Example 1:

# Input: piles = [2,7,9,4,4]

# Output: 10

# Explanation:

# If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
# If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.
# So we return 10 since it's larger.

# Example 2:

# Input: piles = [1,2,3,4,5,100]

# Output: 104

 

# Constraints:

# 1 <= piles.length <= 100
# 1 <= piles[i] <= 104






# Brute force:
def stoneGameII_brute(piles):
    n = len(piles)

    # suffix[i] = piles[i] + piles[i+1] + ...
    suffix = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        suffix[i] = piles[i] + suffix[i + 1]

    def solve(i, M):
        # No piles left
        if i == n:
            return 0

        best = 0

        # Try taking X piles
        for X in range(1, min(2 * M, n - i) + 1):
            next_M = max(M, X)

            # Opponent's best score
            opponent = solve(i + X, next_M)

            # Total stones remaining
            total = suffix[i]

            # Whatever opponent gets, we get the rest
            current = total - opponent

            best = max(best, current)

        return best

    return solve(0, 1)





# Optimal:
class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = piles[i] se end tak total stones
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        memo = {}

        def dp(i, M):
            # Saare piles le liye
            if i == n:
                return 0

            # Already calculated
            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # X piles le sakte hain
            for X in range(1, min(2 * M, n - i) + 1):
                next_M = max(M, X)

                # Opponent maximum kitne stones le sakta hai
                opponent = dp(i + X, next_M)

                # Current player ko remaining mein se opponent ke baad jo bachega
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)