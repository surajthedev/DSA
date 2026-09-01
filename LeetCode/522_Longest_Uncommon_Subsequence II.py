# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
 

# Example 1:

# Input: strs = ["aba","cdc","eae"]
# Output: 3
# Example 2:

# Input: strs = ["aaa","aaa","aa"]
# Output: -1
 

# Constraints:

# 2 <= strs.length <= 50
# 1 <= strs[i].length <= 10
# strs[i] consists of lowercase English letters.







# Solution:
class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def is_subsequence(s, t):
            i = 0

            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1

            return i == len(s)

        # Longest strings first
        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            uncommon = True

            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    uncommon = False
                    break

            if uncommon:
                return len(strs[i])

        return -1