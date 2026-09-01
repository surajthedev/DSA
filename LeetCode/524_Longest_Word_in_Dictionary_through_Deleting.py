# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

 

# Example 1:

# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# Example 2:

# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s and dictionary[i] consist of lowercase English letters.







# Brute force:
class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:

        def is_subsequence(word):
            i = 0

            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1

            return i == len(word)

        ans = ""

        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word

        return ans







# Optimal:
class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        ans = ""

        for word in dictionary:
            i = 0

            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1

            if i == len(word):
                if len(word) > len(ans) or (
                    len(word) == len(ans) and word < ans
                ):
                    ans = word

        return ans