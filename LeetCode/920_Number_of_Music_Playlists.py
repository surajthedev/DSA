# Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

# Every song is played at least once.
# A song can only be played again only if k other songs have been played.
# Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.



# Example 1:

# Input: n = 3, goal = 3, k = 1
# Output: 6
# Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
# Example 2:

# Input: n = 2, goal = 3, k = 0
# Output: 6
# Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
# Example 3:

# Input: n = 2, goal = 3, k = 1
# Output: 2
# Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].


# Constraints:

# 0 <= k < n <= goal <= 100
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
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        def dfs(used, playlist_len):
            if playlist_len == goal:
                return 1 if used == n else 0

            ans = 0

            # Play a new song
            if used < n:
                ans += (n - used) * dfs(used + 1, playlist_len + 1)

            # Replay an old song
            # At most used - k songs are available
            if used > k:
                ans += (used - k) * dfs(used, playlist_len + 1)

            return ans % MOD

        return dfs(0, 0)















# Optimal:
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of playlists of current length
        # containing exactly i unique songs
        dp = [0] * (n + 1)
        dp[0] = 1

        for length in range(goal):
            next_dp = [0] * (n + 1)

            for used in range(n + 1):
                if dp[used] == 0:
                    continue

                # Add a new song
                if used < n:
                    next_dp[used + 1] += dp[used] * (n - used)
                    next_dp[used + 1] %= MOD

                # Replay an old song
                if used > k:
                    next_dp[used] += dp[used] * (used - k)
                    next_dp[used] %= MOD

            dp = next_dp

        return dp[n]
