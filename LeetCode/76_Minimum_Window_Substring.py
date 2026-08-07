# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.


# Brute force:
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        # Required frequency
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        best = ""

        # Every starting point
        for left in range(len(s)):

            # Current window frequency
            window = {}

            # Every ending point
            for right in range(left, len(s)):

                ch = s[right]
                window[ch] = window.get(ch, 0) + 1

                # Check whether current window
                # contains everything from t
                valid = True

                for c in need:
                    if window.get(c, 0) < need[c]:
                        valid = False
                        break

                if valid:
                    current = s[left:right + 1]

                    if best == "" or len(current) < len(best):
                        best = current

                    # Isse chhota same left se nahi milega
                    break

        return best







# Optimal solution:
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        # --------------------------------------------------
        # Required frequency
        # --------------------------------------------------

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # Number of distinct characters in t
        required = len(need)

        # Current window frequency
        window = {}

        # Number of distinct characters whose
        # required frequency has been satisfied
        formed = 0

        left = 0

        # Best answer
        best_len = float('inf')
        best_left = 0
        best_right = 0

        # --------------------------------------------------
        # Expand window using right
        # --------------------------------------------------

        for right in range(len(s)):

            ch = s[right]

            # Character tabhi useful hai
            # jab woh t mein present ho
            if ch in need:

                window[ch] = window.get(ch, 0) + 1

                # Required frequency exactly reach hui
                if window[ch] == need[ch]:
                    formed += 1

            # --------------------------------------------------
            # Window valid hai -> shrink from left
            # --------------------------------------------------

            while formed == required:

                # Current window smaller hai?
                current_len = right - left + 1

                if current_len < best_len:
                    best_len = current_len
                    best_left = left
                    best_right = right

                # Left character remove karo
                left_char = s[left]

                if left_char in need:

                    window[left_char] -= 1

                    # Required frequency se neeche chala gaya
                    if window[left_char] < need[left_char]:
                        formed -= 1

                left += 1

        # No valid window
        if best_len == float('inf'):
            return ""

        return s[best_left:best_right + 1]