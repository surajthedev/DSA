# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.



# Brute Force:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):

            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1

            if j == m:
                return i

        return -1








# Optimal:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)

        # Build LPS
        lps = [0] * m

        length = 0
        i = 1

        while i < m:

            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1

            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Search
        i = 0
        j = 0

        while i < n:

            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == m:
                    return i - j

            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1