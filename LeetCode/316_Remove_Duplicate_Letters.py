# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.







# Brute force:
class Solution:
    def removeDuplicateLetters(self, s):
        result = set()

        def backtrack(index, path):
            if index == len(s):
                if len(set(path)) == len(path):
                    result.add("".join(path))
                return

            # Keep character
            path.append(s[index])
            backtrack(index + 1, path)
            path.pop()

            # Skip character
            backtrack(index + 1, path)

        backtrack(0, [])

        # Only strings containing every unique character
        valid = [
            x for x in result
            if len(x) == len(set(s))
        ]

        return min(valid)






# Optimal:
class Solution:
    def removeDuplicateLetters(self, s):
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            # Already present
            if ch in seen:
                continue

            # Remove bigger characters if they appear later again
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)