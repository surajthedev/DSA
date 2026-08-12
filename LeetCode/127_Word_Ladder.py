# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.






# Brute force:
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for next_word in word_set:
                if next_word in word_set:
                    diff = 0

                    for i in range(len(word)):
                        if word[i] != next_word[i]:
                            diff += 1

                    if diff == 1:
                        queue.append(
                            (next_word, steps + 1)
                        )

                        word_set.remove(next_word)

        return 0









# Optimal:
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)

        # endWord dictionary me nahi hai
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            word_list = list(word)

            for i in range(len(word)):
                original = word_list[i]

                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch == original:
                        continue

                    word_list[i] = ch
                    next_word = ''.join(word_list)

                    if next_word in word_set:
                        # Mark visited
                        word_set.remove(next_word)

                        queue.append(
                            (next_word, steps + 1)
                        )

                word_list[i] = original

        return 0