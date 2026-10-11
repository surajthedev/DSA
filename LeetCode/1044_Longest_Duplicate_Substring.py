# Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

# Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".



# Example 1:

# Input: s = "banana"
# Output: "ana"
# Example 2:

# Input: s = "abcd"
# Output: ""


# Constraints:

# 2 <= s.length <= 3 * 104
# s consists of lowercase English letters.
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
#
#
#
#
#
# ### Brute Force

python
```
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)

        for length in range(n - 1, 0, -1):
            seen = set()

            for i in range(n - length + 1):
                sub = s[i:i + length]

                if sub in seen:
                    return sub

                seen.add(sub)

        return ""
```

### Optimal (Binary Search + Rabin-Karp Rolling Hash)

python
```
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        base = 26
        mod = (1 << 61) - 1

        nums = [ord(c) - ord('a') for c in s]

        def search(length):
            if length == 0:
                return 0

            h = 0
            power = pow(base, length, mod)

            for i in range(length):
                h = (h * base + nums[i]) % mod

            seen = {h: [0]}

            for i in range(1, n - length + 1):
                h = (h * base - nums[i - 1] * power + nums[i + length - 1]) % mod

                if h in seen:
                    for start in seen[h]:
                        if s[start:start + length] == s[i:i + length]:
                            return i

                seen.setdefault(h, []).append(i)

            return -1

        left, right = 1, n - 1
        start = -1
        best = 0

        while left <= right:
            mid = (left + right) // 2
            pos = search(mid)

            if pos != -1:
                best = mid
                start = pos
                left = mid + 1
            else:
                right = mid - 1

        return s[start:start + best] if best else ""
```
