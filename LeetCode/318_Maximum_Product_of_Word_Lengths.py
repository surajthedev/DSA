# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

# Example 1:

# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:

# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:

# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
 

# Constraints:

# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.







# Brute force:
class Solution:
    def maxProduct(self, words):
        n = len(words)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):

                # Check common characters
                if set(words[i]).isdisjoint(set(words[j])):
                    ans = max(
                        ans,
                        len(words[i]) * len(words[j])
                    )

        return ans








# Optimal:
class Solution:
    def maxProduct(self, words):
        n = len(words)

        masks = []
        lengths = []

        for word in words:
            mask = 0

            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            masks.append(mask)
            lengths.append(len(word))

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):

                if masks[i] & masks[j] == 0:
                    ans = max(
                        ans,
                        lengths[i] * lengths[j]
                    )

        return ans