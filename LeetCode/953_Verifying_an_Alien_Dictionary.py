# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
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
#
#
#
#
# Brute force:
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]

            found = False

            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if rank[a[j]] > rank[b[j]]:
                        return False
                    found = True
                    break

            if not found and len(a) > len(b):
                return False

        return True















# Optimal:
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = [0] * 26

        for i, ch in enumerate(order):
            rank[ord(ch) - ord('a')] = i

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]

            for j in range(min(len(a), len(b))):
                x = ord(a[j]) - ord('a')
                y = ord(b[j]) - ord('a')

                if x != y:
                    if rank[x] > rank[y]:
                        return False
                    break
            else:
                if len(a) > len(b):
                    return False

        return True
