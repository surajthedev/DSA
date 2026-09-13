# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

 

# Example 1:

# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
# Example 2:

# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

# Constraints:

# n == stickers.length
# 1 <= n <= 50
# 1 <= stickers[i].length <= 10
# 1 <= target.length <= 15
# stickers[i] and target consist of lowercase English letters.










# Brute Force
class Solution:
    def minStickers(self, stickers, target):
        stickers = [list(s) for s in stickers]

        def dfs(rem):
            if not rem:
                return 0

            ans = float("inf")

            for sticker in stickers:
                temp = rem[:]

                for ch in sticker:
                    if ch in temp:
                        temp.remove(ch)

                if len(temp) < len(rem):
                    res = dfs(temp)
                    if res != -1:
                        ans = min(ans, 1 + res)

            return -1 if ans == float("inf") else ans

        return dfs(list(target))












# Optimal - Bitmask DP
class Solution:
    def minStickers(self, stickers, target):
        m = len(target)
        full = (1 << m) - 1

        sticker_counts = []
        for s in stickers:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            sticker_counts.append(count)

        dp = [float("inf")] * (1 << m)
        dp[0] = 0

        for mask in range(1 << m):
            if dp[mask] == float("inf"):
                continue

            for count in sticker_counts:
                new_mask = mask
                used = count[:]

                for i in range(m):
                    if not (new_mask & (1 << i)):
                        idx = ord(target[i]) - ord('a')

                        if used[idx] > 0:
                            used[idx] -= 1
                            new_mask |= 1 << i

                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)

        return -1 if dp[full] == float("inf") else dp[full]