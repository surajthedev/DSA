# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length






# Brute force:
from collections import Counter

class Solution:
    def characterReplacement(self, s, k):
        n = len(s)
        ans = 0

        for i in range(n):
            count = Counter()

            for j in range(i, n):
                count[s[j]] += 1

                max_freq = max(count.values())
                window_len = j - i + 1

                if window_len - max_freq <= k:
                    ans = max(ans, window_len)

        return ans







# Optimal:
class Solution:
    def characterReplacement(self, s, k):
        count = [0] * 26

        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1

            max_freq = max(max_freq, count[idx])

            window_len = right - left + 1

            if window_len - max_freq > k:
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans