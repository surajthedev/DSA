# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.





# Brute force:
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        n = len(s)
        m = len(p)

        if m > n:
            return []

        target = Counter(p)
        ans = []

        for i in range(n - m + 1):
            window = s[i:i + m]

            if Counter(window) == target:
                ans.append(i)

        return ans





# Optimal:class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        n = len(s)
        m = len(p)

        if m > n:
            return []

        # Frequency of characters in p
        target = [0] * 26

        for ch in p:
            target[ord(ch) - ord('a')] += 1

        # Frequency of current window
        window = [0] * 26

        ans = []

        for i in range(n):
            # Right character add
            window[ord(s[i]) - ord('a')] += 1

            # Window size > m
            if i >= m:
                left_char = s[i - m]
                window[ord(left_char) - ord('a')] -= 1

            # Window size == m
            if window == target:
                ans.append(i - m + 1)

        return ans