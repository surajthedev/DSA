# Given a string licensePlate and an array of strings words, find the shortest completing word in words.

# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

 

# Example 1:

# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.
# Example 2:

# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
 

# Constraints:

# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] consists of lower case English letters.











# Brute force:
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        need = {}

        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] = need.get(ch, 0) + 1

        ans = None

        for word in words:
            count = {}

            for ch in word:
                count[ch] = count.get(ch, 0) + 1

            valid = True

            for ch, freq in need.items():
                if count.get(ch, 0) < freq:
                    valid = False
                    break

            if valid:
                if ans is None or len(word) < len(ans):
                    ans = word

        return ans









# Optimal:
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        need = [0] * 26

        for ch in licensePlate.lower():
            if 'a' <= ch <= 'z':
                need[ord(ch) - ord('a')] += 1

        ans = None
        min_len = float('inf')

        for word in words:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            valid = True

            for i in range(26):
                if count[i] < need[i]:
                    valid = False
                    break

            if valid and len(word) < min_len:
                ans = word
                min_len = len(word)

        return ans