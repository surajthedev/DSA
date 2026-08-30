# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"]

 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 








# Brute force:
class Solution:
    def findWords(self, words):
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]

        ans = []

        for word in words:
            w = word.lower()

            for row in rows:
                if all(ch in row for ch in w):
                    ans.append(word)
                    break

        return ans








# Optimal:
class Solution:
    def findWords(self, words):
        row = {}

        for ch in "qwertyuiop":
            row[ch] = 1

        for ch in "asdfghjkl":
            row[ch] = 2

        for ch in "zxcvbnm":
            row[ch] = 3

        ans = []

        for word in words:
            w = word.lower()

            if all(row[ch] == row[w[0]] for ch in w):
                ans.append(word)

        return ans