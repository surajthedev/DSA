# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.



# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"

# Output: ["sweet","sour"]

# Explanation:

# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# Example 2:

# Input: s1 = "apple apple", s2 = "banana"

# Output: ["banana"]



# Constraints:

# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Brute Force - O(n * m)
class Solution:
    def uncommonFromSentences(self, s1, s2):
        words1 = s1.split()
        words2 = s2.split()

        ans = []

        for word in words1:
            if words1.count(word) == 1 and word not in words2:
                ans.append(word)

        for word in words2:
            if words2.count(word) == 1 and word not in words1:
                ans.append(word)

        return ans











# Optimal - O(n + m)
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1, s2):
        count = Counter((s1 + " " + s2).split())

        return [word for word, freq in count.items() if freq == 1]
