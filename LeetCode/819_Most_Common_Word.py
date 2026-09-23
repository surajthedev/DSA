# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Note that words can not contain punctuation symbols.



# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"


# Constraints:

# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.
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
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        words = []

        word = ""
        for ch in paragraph:
            if ch.isalpha():
                word += ch.lower()
            else:
                if word:
                    words.append(word)
                    word = ""

        if word:
            words.append(word)

        max_count = 0
        answer = ""

        for word in words:
            if word in banned:
                continue

            count = 0
            for w in words:
                if w == word:
                    count += 1

            if count > max_count:
                max_count = count
                answer = word

        return answer








# Optimal;
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)

        words = []
        word = ""

        for ch in paragraph:
            if ch.isalpha():
                word += ch.lower()
            else:
                if word:
                    words.append(word)
                    word = ""

        if word:
            words.append(word)

        count = Counter(words)

        answer = ""
        max_count = 0

        for word, freq in count.items():
            if word not in banned and freq > max_count:
                max_count = freq
                answer = word

        return answer
