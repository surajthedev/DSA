# You are given a palindromic string s.

# Return the lexicographically smallest palindromic permutation of s.

 

# Example 1:

# Input: s = "z"

# Output: "z"

# Explanation:

# A string of only one character is already the lexicographically smallest palindrome.

# Example 2:

# Input: s = "babab"

# Output: "abbba"

# Explanation:

# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

# Example 3:

# Input: s = "daccad"

# Output: "acddca"

# Explanation:

# Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.





# Brute Force Approach:
from itertools import permutations

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ans = None

        for p in set(permutations(s)):
            t = ''.join(p)
            if t == t[::-1]:
                if ans is None or t < ans:
                    ans = t

        return ans




from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        half = []
        middle = ""

        for ch in sorted(freq.keys()):
            half.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                middle = ch

        half = "".join(half)

        return half + middle + half[::-1]