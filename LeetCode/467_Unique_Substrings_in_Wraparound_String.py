# We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so base will look like this:

# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# Given a string s, return the number of unique non-empty substrings of s are present in base.

 

# Example 1:

# Input: s = "a"
# Output: 1
# Explanation: Only the substring "a" of s is in base.
# Example 2:

# Input: s = "cac"
# Output: 2
# Explanation: There are two substrings ("a", "c") of s in base.
# Example 3:

# Input: s = "zab"
# Output: 6
# Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of s in base.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.






# Brute force:
class Solution:
    def findSubstringInWraproundString(self, s):
        n = len(s)
        unique = set()

        for i in range(n):
            current = ""

            for j in range(i, n):
                current += s[j]

                if j == i:
                    unique.add(current)
                else:
                    prev = s[j - 1]
                    curr = s[j]

                    # Check consecutive characters
                    if (ord(curr) - ord(prev)) % 26 == 1:
                        unique.add(current)
                    else:
                        break

        return len(unique)





# Optimal:
class Solution:
    def findSubstringInWraproundString(self, s):

        # dp[i] = longest valid substring
        # ending with character chr(i + ord('a'))
        dp = [0] * 26

        current_length = 0

        for i, ch in enumerate(s):

            # First character OR current char is not
            # consecutive to previous character
            if i == 0 or (ord(ch) - ord(s[i - 1])) % 26 != 1:
                current_length = 1
            else:
                current_length += 1

            index = ord(ch) - ord('a')

            # Keep only the maximum length ending at this char
            dp[index] = max(dp[index], current_length)

        return sum(dp)