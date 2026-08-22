# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.




# Brute force:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i

        return -1





# Optimal:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Count frequency
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Find first character with frequency 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        return -1