# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.



# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
# Example 2:

# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]


# Constraints:

# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.
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
    def findAndReplacePattern(self, words, pattern):
        def matches(word):
            for shift in range(26):
                mapping = {}
                used = set()
                ok = True

                for p, w in zip(pattern, word):
                    p = chr((ord(p) - ord('a') + shift) % 26 + ord('a'))

                    if p in mapping and mapping[p] != w:
                        ok = False
                        break

                    if p not in mapping and w in used:
                        ok = False
                        break

                    mapping[p] = w
                    used.add(w)

                if ok:
                    return True

            return False

        return [word for word in words if matches(word)]













# Optimal:
class Solution:
    def findAndReplacePattern(self, words, pattern):
        def matches(word):
            p_to_w = {}
            w_to_p = {}

            for p, w in zip(pattern, word):
                if p in p_to_w and p_to_w[p] != w:
                    return False

                if w in w_to_p and w_to_p[w] != p:
                    return False

                p_to_w[p] = w
                w_to_p[w] = p

            return True

        return [word for word in words if matches(word)]
