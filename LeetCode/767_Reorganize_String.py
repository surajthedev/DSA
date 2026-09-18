# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.











# Brute Force

class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter

        count = Counter(s)

        def backtrack(path, remaining):
            if len(path) == len(s):
                return "".join(path)

            for ch in count:
                if count[ch] == 0:
                    continue

                if path and path[-1] == ch:
                    continue

                count[ch] -= 1
                path.append(ch)

                result = backtrack(path, remaining - 1)

                if result:
                    return result

                path.pop()
                count[ch] += 1

            return ""

        return backtrack([], len(s))













# Optimal - O(n log 26) ≈ O(n)

class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq

        count = Counter(s)

        if max(count.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        result = []
        prev_freq = 0
        prev_ch = ""

        while heap:
            freq, ch = heapq.heappop(heap)

            result.append(ch)
            freq += 1

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_ch))

            prev_freq = freq
            prev_ch = ch

        return "".join(result)