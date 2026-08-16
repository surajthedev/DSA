# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "f11", t = "b23"

# Output: false

# Explanation:

# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.









# Brute force:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            # s -> t mapping already exists
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False

            # t -> s mapping already exists
            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False

            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return True








# Optimal:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = [-1] * 128
        t_to_s = [-1] * 128

        for i in range(len(s)):
            a = ord(s[i])
            b = ord(t[i])

            if s_to_t[a] != -1 and s_to_t[a] != b:
                return False

            if t_to_s[b] != -1 and t_to_s[b] != a:
                return False

            s_to_t[a] = b
            t_to_s[b] = a

        return True