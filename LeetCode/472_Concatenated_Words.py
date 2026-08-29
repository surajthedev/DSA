# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

 

# Example 1:

# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Example 2:

# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
 

# Constraints:

# 1 <= words.length <= 104
# 1 <= words[i].length <= 30
# words[i] consists of only lowercase English letters.
# All the strings of words are unique.
# 1 <= sum(words[i].length) <= 105






# Brute force:
class Solution:
    def findAllConcatenatedWordsInADict(self, words):

        word_set = set(words)
        result = []

        def can_form(word):
            n = len(word)

            # dp[i] = whether word[:i] can be formed
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):

                for j in range(i):

                    if not dp[j]:
                        continue

                    if word[j:i] in word_set:
                        dp[i] = True
                        break

            return dp[n]

        for word in words:

            # Temporarily remove current word
            word_set.remove(word)

            if can_form(word):
                result.append(word)

            word_set.add(word)

        return result






# Optimal:
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:

    def findAllConcatenatedWordsInADict(self, words):

        # -------------------------
        # Build Trie
        # -------------------------

        root = TrieNode()

        for word in words:

            node = root

            for ch in word:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.is_word = True

        # -------------------------
        # Check each word
        # -------------------------

        result = []

        for word in words:

            n = len(word)

            # memo[i] = True/False
            # whether word[i:] can be formed
            memo = {}

            def dfs(start, count):

                # Reached end
                if start == n:
                    return count >= 2

                if start in memo:
                    return memo[start]

                node = root

                for end in range(start, n):

                    ch = word[end]

                    if ch not in node.children:
                        break

                    node = node.children[ch]

                    # Found a dictionary word
                    if node.is_word:

                        if dfs(end + 1, count + 1):
                            memo[start] = True
                            return True

                memo[start] = False
                return False

            if dfs(0, 0):
                result.append(word)

        return result