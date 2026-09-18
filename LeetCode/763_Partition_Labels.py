# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.








# Brute Force

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        n = len(s)
        result = []
        start = 0

        while start < n:
            chars = set()
            end = start

            while end < n:
                chars.add(s[end])

                valid = True
                for i in range(end + 1, n):
                    if s[i] in chars:
                        valid = False
                        break

                if valid:
                    result.append(end - start + 1)
                    start = end + 1
                    break

                end += 1

        return result












# Optimal - O(n)

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        result = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result