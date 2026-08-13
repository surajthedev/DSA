# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.




# Brute force:
class Solution:
    def wordBreak(self, s, wordDict):
        result = []

        def backtrack(start, path):
            # Entire string consumed
            if start == len(s):
                result.append(" ".join(path))
                return

            for word in wordDict:
                end = start + len(word)

                if end <= len(s) and s[start:end] == word:
                    path.append(word)

                    backtrack(end, path)

                    path.pop()

        backtrack(0, [])

        return result






# Optimal:
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        maxLen = max(map(len, wordDict))

        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []

            end_limit = min(len(s), start + maxLen)

            for end in range(start + 1, end_limit + 1):
                word = s[start:end]

                if word not in wordSet:
                    continue

                for sentence in dfs(end):
                    if sentence:
                        result.append(word + " " + sentence)
                    else:
                        result.append(word)

            memo[start] = result
            return result

        return dfs(0)