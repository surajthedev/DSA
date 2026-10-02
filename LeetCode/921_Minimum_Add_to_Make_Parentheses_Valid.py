# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.



# Example 1:

# Input: s = "())"
# Output: 1
# Example 2:

# Input: s = "((("
# Output: 3


# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
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
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)

        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == "(":
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        def dfs(s):
            if is_valid(s):
                return 0

            ans = float("inf")

            for i in range(len(s) + 1):
                ans = min(ans, 1 + dfs(s[:i] + "(" + s[i:]))
                ans = min(ans, 1 + dfs(s[:i] + ")" + s[i:]))

            return ans

        return dfs(s)












# Optimal:
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0

        for ch in s:
            if ch == "(":
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1

        # Remaining '(' need closing ')'
        return additions + balance
