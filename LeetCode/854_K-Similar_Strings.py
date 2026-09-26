# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.



# Example 1:

# Input: s1 = "ab", s2 = "ba"
# Output: 1
# Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
# Example 2:

# Input: s1 = "abc", s2 = "bca"
# Output: 2
# Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".


# Constraints:

# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
# s2 is an anagram of s1.
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
from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        q = deque([(s1, 0)])
        visited = {s1}

        while q:
            s, steps = q.popleft()

            i = 0
            while i < len(s) and s[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    chars = list(s)
                    chars[i], chars[j] = chars[j], chars[i]
                    nxt = ''.join(chars)

                    if nxt == s2:
                        return steps + 1

                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

        return -1









# Optimal:
from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        q = deque([s1])
        visited = {s1}
        steps = 0

        while q:
            for _ in range(len(q)):
                s = q.popleft()

                i = 0
                while s[i] == s2[i]:
                    i += 1

                for j in range(i + 1, len(s)):
                    if s[j] == s2[i] and s[j] != s2[j]:
                        chars = list(s)
                        chars[i], chars[j] = chars[j], chars[i]
                        nxt = ''.join(chars)

                        if nxt == s2:
                            return steps + 1

                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)

            steps += 1

        return -1
