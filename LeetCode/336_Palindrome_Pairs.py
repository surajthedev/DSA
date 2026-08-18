# You are given a 0-indexed array of unique strings words.

# A palindrome pair is a pair of integers (i, j) such that:

# 0 <= i, j < words.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a palindrome.
# Return an array of all the palindrome pairs of words.

# You must write an algorithm with O(sum of words[i].length) runtime complexity.

 

# Example 1:

# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
# Example 2:

# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:

# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["a","a"]
 

# Constraints:

# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lowercase English letters.




# Brute force:
class Solution:
    def palindromePairs(self, words):
        ans = []

        def is_palindrome(s):
            return s == s[::-1]

        n = len(words)

        for i in range(n):
            for j in range(n):
                if i != j:
                    if is_palindrome(words[i] + words[j]):
                        ans.append([i, j])

        return ans






# Optimal:
class Solution:
    def palindromePairs(self, words):
        ans = []
        
        # word -> index
        mp = {}

        for i, word in enumerate(words):
            mp[word] = i

        def is_palindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            length = len(word)

            for j in range(length + 1):
                left = word[:j]
                right = word[j:]

                # left is palindrome
                # reverse(right) + word
                if is_palindrome(left):
                    rev = right[::-1]

                    if rev in mp and mp[rev] != i:
                        ans.append([mp[rev], i])

                # right is palindrome
                # word + reverse(left)
                if j != length and is_palindrome(right):
                    rev = left[::-1]

                    if rev in mp and mp[rev] != i:
                        ans.append([i, mp[rev]])

        return ans