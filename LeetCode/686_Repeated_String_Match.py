# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

# Example 1:

# Input: a = "abcd", b = "cdabcdab"
# Output: 3
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
# Example 2:

# Input: a = "a", b = "aa"
# Output: 2
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist of lowercase English letters.








# Brute force:
class Solution:
    def repeatedStringMatch(self, a, b):
        repeated = ""
        count = 0

        while len(repeated) < len(b) + len(a):
            repeated += a
            count += 1

            if b in repeated:
                return count

        return -1










# Optimal:
class Solution:
    def repeatedStringMatch(self, a, b):
        def kmp(text, pattern):
            lps = [0] * len(pattern)

            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1

                lps[i] = j

            j = 0

            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]

                if text[i] == pattern[j]:
                    j += 1

                if j == len(pattern):
                    return True

            return False

        count = (len(b) + len(a) - 1) // len(a)

        text = a * count

        if kmp(text, b):
            return count

        if kmp(text + a, b):
            return count + 1

        return -1