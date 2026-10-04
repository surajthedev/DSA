# Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

# You may assume that no string in words is a substring of another string in words.



# Example 1:

# Input: words = ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
# Example 2:

# Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"


# Constraints:

# 1 <= words.length <= 12
# 1 <= words[i].length <= 20
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
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
#
#
#
# # Brute Force - Backtracking
class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        overlap = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                max_overlap = min(len(words[i]), len(words[j]))

                for k in range(max_overlap, 0, -1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k
                        break

        best = None

        def backtrack(path, used):
            nonlocal best

            if len(path) == n:
                result = words[path[0]]

                for i in range(1, n):
                    result += words[path[i]][overlap[path[i - 1]][path[i]]:]

                if best is None or len(result) < len(best):
                    best = result

                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(i)

                    backtrack(path, used)

                    path.pop()
                    used[i] = False

        backtrack([], [False] * n)

        return best
















# Optimal - Bitmask DP
class Solution:
    def shortestSuperstring(self, words):
        n = len(words)

        overlap = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k
                        break

        # dp[mask][i] = maximum total overlap
        # when using words in mask and ending at i
        dp = [[-1] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(1 << n):
            for last in range(n):
                if dp[mask][last] == -1:
                    continue

                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue

                    new_mask = mask | (1 << nxt)
                    value = dp[mask][last] + overlap[last][nxt]

                    if value > dp[new_mask][nxt]:
                        dp[new_mask][nxt] = value
                        parent[new_mask][nxt] = last

        mask = (1 << n) - 1
        last = max(range(n), key=lambda i: dp[mask][i])

        order = []

        while last != -1:
            order.append(last)
            prev = parent[mask][last]

            if prev == -1:
                break

            mask ^= 1 << last
            last = prev

        order.reverse()

        result = words[order[0]]

        for i in range(1, n):
            prev = order[i - 1]
            curr = order[i]

            result += words[curr][overlap[prev][curr]:]

        return result
