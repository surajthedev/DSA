# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

 

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.



# Brute force:
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        def is_palindrome(left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        n = len(s)

        # Longest palindromic prefix
        for end in range(n - 1, -1, -1):

            if is_palindrome(0, end):

                suffix = s[end + 1:]

                return suffix[::-1] + s

        return s







# Optimal:
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        rev = s[::-1]

        combined = s + "#" + rev

        lps = [0] * len(combined)

        for i in range(1, len(combined)):

            j = lps[i - 1]

            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        longest_pal_prefix = lps[-1]

        suffix = s[longest_pal_prefix:]

        return suffix[::-1] + s