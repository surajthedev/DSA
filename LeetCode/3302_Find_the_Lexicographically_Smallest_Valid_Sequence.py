# You are given two strings word1 and word2.

# A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

# A sequence of indices seq is called valid if:

# The indices are sorted in ascending order.
# Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
# Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.

# Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

 

# Example 1:

# Input: word1 = "vbcca", word2 = "abc"

# Output: [0,1,2]

# Explanation:

# The lexicographically smallest valid sequence of indices is [0, 1, 2]:

# Change word1[0] to 'a'.
# word1[1] is already 'b'.
# word1[2] is already 'c'.
# Example 2:

# Input: word1 = "bacdc", word2 = "abc"

# Output: [1,2,4]

# Explanation:

# The lexicographically smallest valid sequence of indices is [1, 2, 4]:

# word1[1] is already 'a'.
# Change word1[2] to 'b'.
# word1[4] is already 'c'.
# Example 3:

# Input: word1 = "aaaaaa", word2 = "aaabc"

# Output: []

# Explanation:

# There is no valid sequence of indices.

# Example 4:

# Input: word1 = "abc", word2 = "ab"

# Output: [0,1]

 

# Constraints:

# 1 <= word2.length < word1.length <= 3 * 105
# word1 and word2 consist only of lowercase English letters.




# Brute force:
from itertools import combinations


class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        best = None

        for indices in combinations(range(n), m):
            mismatches = 0

            for j, i in enumerate(indices):
                if word1[i] != word2[j]:
                    mismatches += 1

                    if mismatches > 1:
                        break

            if mismatches <= 1:
                if best is None or indices < best:
                    best = indices

        return list(best) if best is not None else []




# Optimal:
class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # last[j] = rightmost index in word1 from which
        # word2[j:] can be matched exactly.
        last = [-1] * m

        i = n - 1
        j = m - 1

        # Build last[] from right to left
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        ans = []

        j = 0
        mismatch_used = False

        # Greedily choose the smallest possible index
        for i in range(n):

            if j == m:
                break

            # Case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: use our one allowed mismatch
            elif not mismatch_used:
                # We can use i as mismatch only if
                # the remaining suffix can still be matched.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    mismatch_used = True

        if j == m:
            return ans

        return []