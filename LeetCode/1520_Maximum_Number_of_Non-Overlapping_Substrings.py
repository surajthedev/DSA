# Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

# The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
# A substring that contains a certain character c must also contain all occurrences of c.
# Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

# Notice that you can return the substrings in any order.

 

# Example 1:

# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the conditions:
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
# Example 2:

# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

# Constraints:

# 1 <= s.length <= 105
# s contains only lowercase English letters.









# Brute force:
# Brute Force

class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        for c in range(26):
            if last[c] == -1:
                continue

            l, r = first[c], last[c]
            valid = True
            i = l

            while i <= r:
                idx = ord(s[i]) - ord('a')

                if first[idx] < l:
                    valid = False
                    break

                r = max(r, last[idx])
                i += 1

            if valid:
                intervals.append((l, r))

        # Try all subsets of valid intervals
        m = len(intervals)
        best_count = 0
        best_length = float('inf')
        best = []

        def dfs(i, selected, last_end, total_len):
            nonlocal best_count, best_length, best

            if i == m:
                count = len(selected)

                if count > best_count or (
                    count == best_count and total_len < best_length
                ):
                    best_count = count
                    best_length = total_len
                    best = selected[:]
                return

            dfs(i + 1, selected, last_end, total_len)

            l, r = intervals[i]

            if l > last_end:
                selected.append(i)
                dfs(
                    i + 1,
                    selected,
                    r,
                    total_len + (r - l + 1)
                )
                selected.pop()

        dfs(0, [], -1, 0)

        return [s[intervals[i][0]:intervals[i][1] + 1] for i in best]










# Optimal:
# Optimal - O(n)

class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        for c in range(26):
            if last[c] == -1:
                continue

            l, r = first[c], last[c]
            i = l
            valid = True

            while i <= r:
                idx = ord(s[i]) - ord('a')

                if first[idx] < l:
                    valid = False
                    break

                r = max(r, last[idx])
                i += 1

            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for l, r in intervals:
            if l > end:
                result.append(s[l:r + 1])
                end = r

        return result