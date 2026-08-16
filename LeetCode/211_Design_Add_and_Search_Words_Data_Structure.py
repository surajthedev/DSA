# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.





# Brute force:
class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:

        for stored_word in self.words:

            if len(stored_word) != len(word):
                continue

            match = True

            for a, b in zip(stored_word, word):

                if b != '.' and a != b:
                    match = False
                    break

            if match:
                return True

        return False







# Optimal:
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        curr = self.root

        for ch in word:

            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, index):

            # Complete word check
            if index == len(word):
                return node.is_end

            ch = word[index]

            # Normal character
            if ch != '.':
                if ch not in node.children:
                    return False

                return dfs(node.children[ch], index + 1)

            # '.' → try every child
            for child in node.children.values():

                if dfs(child, index + 1):
                    return True

            return False

        return dfs(self.root, 0)