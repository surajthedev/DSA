# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

 

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
 

# Constraints:

# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.






# Brute Force
class Solution:
    def replaceWords(self, dictionary, sentence):
        words = sentence.split()
        result = []

        for word in words:
            shortest = word

            for root in dictionary:
                if word.startswith(root) and len(root) < len(shortest):
                    shortest = root

            result.append(shortest)

        return " ".join(result)











# Optimal:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def replaceWords(self, dictionary, sentence):
        root = TrieNode()

        # Build Trie
        for word in dictionary:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

            node.is_end = True

        def find_root(word):
            node = root
            prefix = []

            for ch in word:
                if ch not in node.children:
                    return word

                node = node.children[ch]
                prefix.append(ch)

                if node.is_end:
                    return "".join(prefix)

            return word

        return " ".join(find_root(word) for word in sentence.split())