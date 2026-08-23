# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

# if no such substring exists, return 0.

 

# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 105






# Brute force:
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        answer = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                # Check whether every character appears >= k times
                valid = True

                for count in freq:
                    if count > 0 and count < k:
                        valid = False
                        break

                if valid:
                    answer = max(answer, j - i + 1)

        return answer







# Optimal:
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def solve(left, right):
            # Substring is too small
            if right - left < k:
                return 0

            # Frequency count
            freq = [0] * 26

            for i in range(left, right):
                freq[ord(s[i]) - ord('a')] += 1

            # Find a character that occurs less than k times
            for i in range(left, right):
                index = ord(s[i]) - ord('a')

                if freq[index] < k:
                    # Split around this invalid character
                    j = i + 1

                    while j < right and freq[ord(s[j]) - ord('a')] < k:
                        j += 1

                    left_part = solve(left, i)
                    right_part = solve(j, right)

                    return max(left_part, right_part)

            # Every character occurs at least k times
            return right - left

        return solve(0, len(s))