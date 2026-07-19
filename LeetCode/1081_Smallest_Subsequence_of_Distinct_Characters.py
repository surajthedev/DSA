# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.



# Brute Force:
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        unique = set(s)
        n = len(s)
        ans = None

        def backtrack(idx, curr):
            nonlocal ans

            if idx == n:
                if len(set(curr)) == len(curr) and set(curr) == unique:
                    candidate = "".join(curr)
                    if ans is None or candidate < ans:
                        ans = candidate
                return

            # Take
            curr.append(s[idx])
            backtrack(idx + 1, curr)
            curr.pop()

            # Not Take
            backtrack(idx + 1, curr)

        backtrack(0, [])
        return ans







# Optimal Approach:
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):

            if ch in visited:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)