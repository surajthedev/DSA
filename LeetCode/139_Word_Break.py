# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.





# Brute force:
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)

        def dfs(start):
            # Entire string consumed
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    if dfs(end):
                        return True

            return False

        return dfs(0)








# Optimal:
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)

        # Empty string can be segmented
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]