# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# The sum of all shortest transformation sequences does not exceed 105.



# Brute force:
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)

        if endWord not in word_set:
            return []

        result = []

        def is_one_letter_diff(word1, word2):
            diff = 0

            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1

            return diff == 1

        def dfs(word, path, visited):
            if word == endWord:
                result.append(path[:])
                return

            for next_word in word_set:
                if next_word not in visited:
                    if is_one_letter_diff(word, next_word):
                        visited.add(next_word)
                        path.append(next_word)

                        dfs(next_word, path, visited)

                        path.pop()
                        visited.remove(next_word)

        dfs(beginWord, [beginWord], {beginWord})

        # Brute force me saare paths aa sakte hain.
        if not result:
            return []

        min_length = min(len(path) for path in result)

        return [
            path for path in result
            if len(path) == min_length
        ]







# Optimal:
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)

        if endWord not in word_set:
            return []

        # parents[word] = all previous words
        # that can reach word through a shortest path
        parents = defaultdict(list)

        # BFS distance
        distance = {beginWord: 0}

        queue = deque([beginWord])

        found = False

        while queue and not found:
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        next_word = (
                            word[:i] + ch + word[i + 1:]
                        )

                        if next_word not in word_set:
                            continue

                        new_distance = distance[word] + 1

                        # First time discovering this word
                        if next_word not in distance:
                            distance[next_word] = new_distance
                            parents[next_word].append(word)
                            queue.append(next_word)

                        # Another shortest way to reach it
                        elif distance[next_word] == new_distance:
                            parents[next_word].append(word)

                        if next_word == endWord:
                            found = True

            # We finish this entire BFS level before stopping

        if endWord not in distance:
            return []

        # Backtracking from endWord to beginWord
        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)

                backtrack(parent)

                path.pop()

        backtrack(endWord)

        return result