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
# Brute Force
from itertools import product

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)

        for k in range(n + 1):
            for additions in product("()", repeat=k):
                t = list(s)

                # Try every possible insertion arrangement recursively
                def valid(i, j, balance):
                    if balance < 0:
                        return False
                    if i == len(t) and j == k:
                        return balance == 0

                    if i < len(t) and valid(i + 1, j, balance + (1 if t[i] == '(' else -1)):
                        return True

                    if j < k:
                        ch = additions[j]
                        if valid(i, j + 1, balance + (1 if ch == '(' else -1)):
                            return True

                    return False

                if valid(0, 0, 0):
                    return k

        return n


# Optimal - O(n) Time, O(1) Space
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    ans += 1

        return ans + balance
