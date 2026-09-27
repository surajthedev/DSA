# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


# Example 1:

# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
# Example 2:

# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
# Example 3:

# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.


# Constraints:

# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.
#
#
#
#
#
#
#
#
# Brute force:
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)

        for i in range(n):
            for j in range(i + 1, n):
                chars = list(s)
                chars[i], chars[j] = chars[j], chars[i]

                if ''.join(chars) == goal:
                    return True

        return False










# Optimal:
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        diff = []

        for a, b in zip(s, goal):
            if a != b:
                diff.append((a, b))

        if len(diff) == 2:
            return diff[0] == diff[1][::-1]

        if len(diff) == 0:
            return len(set(s)) < len(s)

        return False
