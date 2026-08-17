# There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

# In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

# The game ends when there is only one stone remaining. Alice's score is initially zero.

# Return the maximum score that Alice can obtain.

 

# Example 1:

# Input: stoneValue = [6,2,3,4,5,5]
# Output: 18
# Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
# In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
# The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
# Example 2:

# Input: stoneValue = [7,7,7,7,7,7,7]
# Output: 28
# Example 3:

# Input: stoneValue = [4]
# Output: 0
 

# Constraints:

# 1 <= stoneValue.length <= 500
# 1 <= stoneValue[i] <= 106







# Optimal Solution:
class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] =
        # maximum score Alice can get from l..r
        dp = [[0] * n for _ in range(n)]

        # left_best[l][r] =
        # max(dp[l][k] + sum(l..k)) for l <= k <= r
        #
        # This is useful when left side survives.
        left_best = [[0] * n for _ in range(n)]

        # right_best[l][r] =
        # max(dp[k][r] + sum(k..r)) for l <= k <= r
        #
        # This is useful when right side survives.
        right_best = [[0] * n for _ in range(n)]

        # Base case: one stone
        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        # Build intervals by increasing length
        for length in range(2, n + 1):

            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                # -------------------------------------------------
                # Binary search:
                #
                # Find largest k such that
                #
                # sum(l..k) <= sum(k+1..r)
                #
                # Because all values are positive, this condition
                # is monotonic.
                # -------------------------------------------------

                low = l
                high = r - 1

                while low <= high:
                    mid = (low + high) // 2

                    left_sum = prefix[mid + 1] - prefix[l]

                    if left_sum * 2 <= total:
                        low = mid + 1
                    else:
                        high = mid - 1

                # high = last split where left_sum <= right_sum
                split = high

                best = 0

                # -------------------------------------------------
                # Case 1:
                # left_sum <= right_sum
                #
                # Left side survives.
                #
                # All splits from l to split are possible.
                # left_best gives the best one in O(1).
                # -------------------------------------------------

                if split >= l:
                    best = max(
                        best,
                        left_best[l][split]
                    )

                # -------------------------------------------------
                # Equality case:
                #
                # If left_sum == right_sum, Alice can choose either
                # side.
                # -------------------------------------------------

                if split >= l:
                    left_sum = prefix[split + 1] - prefix[l]

                    if left_sum * 2 == total:
                        best = max(
                            best,
                            right_best[split + 1][r]
                        )

                # -------------------------------------------------
                # Case 2:
                # left_sum > right_sum
                #
                # Right side survives.
                #
                # Valid splits are split+1 ... r-1.
                #
                # Right side starts at k+1, therefore the first
                # possible right interval starts at split+2.
                # -------------------------------------------------

                if split + 2 <= r:
                    best = max(
                        best,
                        right_best[split + 2][r]
                    )

                dp[l][r] = best

                # -------------------------------------------------
                # Update left_best
                #
                # dp[l][r] + sum(l..r)
                # -------------------------------------------------

                current_sum = prefix[r + 1] - prefix[l]

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r] + current_sum
                )

                # -------------------------------------------------
                # Update right_best
                # -------------------------------------------------

                right_best[l][r] = max(
                    right_best[l + 1][r],
                    dp[l][r] + current_sum
                )

        return dp[0][n - 1]