# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104







# Brute force:
class Solution:
    def reverseStr(self, s, k):
        s = list(s)

        for start in range(0, len(s), 2 * k):
            end = min(start + k, len(s))
            s[start:end] = reversed(s[start:end])

        return ''.join(s)








# Optimal:
class Solution:
    def reverseStr(self, s, k):
        result = []

        for i in range(0, len(s), 2 * k):
            part = s[i:i + k][::-1]
            result.append(part)
            result.append(s[i + k:i + 2 * k])

        return ''.join(result)