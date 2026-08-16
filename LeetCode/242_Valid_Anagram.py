# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.






# Brute force:
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)






# Optimal:
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        return all(x == 0 for x in count)