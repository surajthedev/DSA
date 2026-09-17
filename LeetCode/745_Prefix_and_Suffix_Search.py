# Design a special dictionary that searches the words in it by a prefix and a suffix.

# Implement the WordFilter class:

# WordFilter(string[] words) Initializes the object with the words in the dictionary.
# f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

# Example 1:

# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
 

# Constraints:

# 1 <= words.length <= 104
# 1 <= words[i].length <= 7
# 1 <= pref.length, suff.length <= 7
# words[i], pref and suff consist of lowercase English letters only.
# At most 104 calls will be made to the function f.










# Brute force:
class WordFilter:

    def __init__(self, words):
        self.words = words

    def f(self, pref, suff):
        for i in range(len(self.words) - 1, -1, -1):
            word = self.words[i]

            if word.startswith(pref) and word.endswith(suff):
                return i

        return -1









# Optimal:
class WordFilter:

    def __init__(self, words):
        self.mp = {}

        for i, word in enumerate(words):
            n = len(word)

            for p in range(n + 1):
                for s in range(n + 1):
                    key = word[:p] + "#" + word[n - s:]
                    self.mp[key] = i

    def f(self, pref, suff):
        return self.mp.get(pref + "#" + suff, -1)