# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.













# Brute Force
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            i = 0

            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1

            return i == len(word)

        return sum(is_subsequence(word) for word in words)












# Optimal
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = [[] for _ in range(26)]

        for word in words:
            buckets[ord(word[0]) - ord('a')].append((word, 0))

        ans = 0

        for ch in s:
            idx = ord(ch) - ord('a')
            current = buckets[idx]
            buckets[idx] = []

            for word, i in current:
                i += 1

                if i == len(word):
                    ans += 1
                else:
                    buckets[ord(word[i]) - ord('a')].append((word, i))

        return ans