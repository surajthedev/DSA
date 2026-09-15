# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

# Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

# Example 1:

# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:

# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# words[i] consists of lowercase English letters.









# Brute Force
class Solution:
    def longestWord(self, words: list[str]) -> str:
        word_set = set(words)
        ans = ""

        for word in words:
            valid = True

            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break

            if valid:
                if len(word) > len(ans) or (
                    len(word) == len(ans) and word < ans
                ):
                    ans = word

        return ans













# Optimal - Sorting
class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()

        built = {""}
        ans = ""

        for word in words:
            if word[:-1] in built:
                built.add(word)

                if len(word) > len(ans):
                    ans = word

        return ans
