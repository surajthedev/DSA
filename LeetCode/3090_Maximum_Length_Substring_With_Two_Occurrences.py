# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.






# Brute force:
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                freq = [0] * 26
                valid = True

                for k in range(i, j + 1):
                    idx = ord(s[k]) - ord('a')
                    freq[idx] += 1

                    if freq[idx] > 2:
                        valid = False
                        break

                if valid:
                    ans = max(ans, j - i + 1)

        return ans







# Optimal:
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = [0] * 26

        left = 0
        ans = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('a')
            freq[idx] += 1

            # Window invalid hai
            while freq[idx] > 2:
                left_idx = ord(s[left]) - ord('a')
                freq[left_idx] -= 1
                left += 1

            # Current window valid hai
            ans = max(ans, right - left + 1)

        return ans