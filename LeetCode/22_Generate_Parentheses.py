# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8
#
#
#
#
#
#
# Brute force:
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

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

        def generate(s):
            if len(s) == 2 * n:
                if is_valid(s):
                    result.append(s)
                return

            generate(s + "(")
            generate(s + ")")

        generate("")
        return result
















# Optimal:
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                result.append(s)
                return

            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
