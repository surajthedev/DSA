# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.



# Example 1:

# Input: s = "()())()"
# Output: ["(())()","()()()"]
# Example 2:

# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# Example 3:

# Input: s = ")("
# Output: [""]


# Constraints:

# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.
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
# Brute force:
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)

        def is_valid(t):
            balance = 0
            for ch in t:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        for remove_count in range(n + 1):
            ans = set()

            def generate(start, removed, path):
                if removed == remove_count:
                    t = ''.join(path)
                    if is_valid(t):
                        ans.add(t)
                    return

                for i in range(start, n):
                    path.append(s[i])
                    generate(i + 1, removed + 1, path)
                    path.pop()

            generate(0, 0, [])

            if ans:
                return list(ans)

        return [""]












# Oprimal:
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(t):
            balance = 0

            for ch in t:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}

        while queue:
            ans = []

            for cur in queue:
                if is_valid(cur):
                    ans.append(cur)

            if ans:
                return list(set(ans))

            next_level = []

            for cur in queue:
                for i in range(len(cur)):
                    if cur[i].isalpha():
                        continue

                    nxt = cur[:i] + cur[i + 1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        next_level.append(nxt)

            queue = next_level

        return [""]
