# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.



# Example 1:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

# Output: ["facebook","google","leetcode"]

# Example 2:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

# Output: ["leetcode"]

# Example 3:

# Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

# Output: ["cccbb"]



# Constraints:

# 1 <= words1.length, words2.length <= 104
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters.
# All the strings of words1 are unique.
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
# Brute force:
from collections import Counter

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        result = []

        for word in words1:
            word_count = Counter(word)
            universal = True

            for target in words2:
                target_count = Counter(target)

                for ch, count in target_count.items():
                    if word_count[ch] < count:
                        universal = False
                        break

                if not universal:
                    break

            if universal:
                result.append(word)

        return result











# Optimal:
class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        required = [0] * 26

        # Maximum frequency required for each character
        for word in words2:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                required[i] = max(required[i], count[i])

        result = []

        for word in words1:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            if all(count[i] >= required[i] for i in range(26)):
                result.append(word)

        return result
