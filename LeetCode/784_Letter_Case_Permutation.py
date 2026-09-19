# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]
 

# Constraints:

# 1 <= s.length <= 12








# Brute Force

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        letters = [i for i, ch in enumerate(s) if ch.isalpha()]
        n = len(letters)
        result = []

        for mask in range(1 << n):
            chars = list(s)

            for j, idx in enumerate(letters):
                if mask & (1 << j):
                    chars[idx] = chars[idx].upper()
                else:
                    chars[idx] = chars[idx].lower()

            result.append("".join(chars))

        return result












# Optimal:
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        chars = list(s)

        def backtrack(i):
            if i == len(chars):
                result.append("".join(chars))
                return

            if chars[i].isalpha():
                chars[i] = chars[i].lower()
                backtrack(i + 1)

                chars[i] = chars[i].upper()
                backtrack(i + 1)
            else:
                backtrack(i + 1)

        backtrack(0)
        return result