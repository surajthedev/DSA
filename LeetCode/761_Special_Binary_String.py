# Special binary strings are binary strings with the following two properties:

# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# You are given a special binary string s.

# A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

# Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

 

# Example 1:

# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.
# Example 2:

# Input: s = "10"
# Output: "10"
 

# Constraints:

# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.










# Brute Force

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        seen = {s}
        stack = [s]
        best = s

        while stack:
            cur = stack.pop()
            best = max(best, cur)

            n = len(cur)

            for i in range(n):
                balance = 0

                for j in range(i, n):
                    balance += 1 if cur[j] == '1' else -1

                    if balance != 0:
                        continue

                    a = cur[i:j + 1]

                    if i > 0:
                        balance2 = 0
                        for k in range(i):
                            balance2 += 1 if cur[k] == '1' else -1
                            if balance2 < 0:
                                break
                        else:
                            if j + 1 < n:
                                b = cur[j + 1:]
                                if b and a + b != cur and a + b in seen:
                                    pass

                    for k in range(j + 1, n):
                        balance2 = 0
                        for x in range(k, n):
                            balance2 += 1 if cur[x] == '1' else -1
                            if balance2 < 0:
                                break

                            if balance2 == 0:
                                b = cur[k:x + 1]

                                if k == j + 1:
                                    new_s = cur[:i] + b + a + cur[x + 1:]

                                    if new_s not in seen:
                                        seen.add(new_s)
                                        stack.append(new_s)
                                break

        return best














# Optimal - Recursive + Sorting

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        count = 0
        start = 0

        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1

            if count == 0:
                inner = s[start + 1:i]
                parts.append("1" + self.makeLargestSpecial(inner) + "0")
                start = i + 1

        parts.sort(reverse=True)

        return "".join(parts)