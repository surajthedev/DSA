# A valid encoding of an array of words is any reference string s and array of indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.



# Example 1:

# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
# Example 2:

# Input: words = ["t"]
# Output: 2
# Explanation: A valid encoding would be s = "t#" and indices = [0].


# Constraints:

# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# words[i] consists of only lowercase letters.
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
class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        words = list(set(words))
        n = len(words)
        total = 0

        for i in range(n):
            is_suffix = False

            for j in range(n):
                if i != j and words[j].endswith(words[i]):
                    is_suffix = True
                    break

            if not is_suffix:
                total += len(words[i]) + 1

        return total








# Optimal:
class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        words = list(set(words))

        root = TrieNode()
        nodes = []

        for word in words:
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            nodes.append((node, len(word)))

        ans = 0

        for node, length in nodes:
            if not node.children:
                ans += length + 1

        return ans
