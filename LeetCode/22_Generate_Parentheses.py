# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8



# Brute Force:
class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def isValid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                else:
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        def generate(curr):
            if len(curr) == 2 * n:
                if isValid(curr):
                    ans.append(curr)
                return

            generate(curr + "(")
            generate(curr + ")")

        generate("")
        return ans









# Optimal Approach:
class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def backtrack(curr, openCount, closeCount):

            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if openCount < n:
                backtrack(curr + "(", openCount + 1, closeCount)

            if closeCount < openCount:
                backtrack(curr + ")", openCount, closeCount + 1)

        backtrack("", 0, 0)
        return ans