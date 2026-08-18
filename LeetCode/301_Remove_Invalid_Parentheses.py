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





# Brute force:
class Solution:
    def removeInvalidParentheses(self, s):
        left_remove = 0
        right_remove = 0

        # Find minimum number of invalid parentheses
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, left, right, balance, path):
            if index == len(s):
                if left == 0 and right == 0 and balance == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            if ch == '(':
                # Remove '('
                if left > 0:
                    backtrack(
                        index + 1,
                        left - 1,
                        right,
                        balance,
                        path
                    )

                # Keep '('
                path.append(ch)
                backtrack(
                    index + 1,
                    left,
                    right,
                    balance + 1,
                    path
                )
                path.pop()

            elif ch == ')':
                # Remove ')'
                if right > 0:
                    backtrack(
                        index + 1,
                        left,
                        right - 1,
                        balance,
                        path
                    )

                # Keep ')' only if it has matching '('
                if balance > 0:
                    path.append(ch)
                    backtrack(
                        index + 1,
                        left,
                        right,
                        balance - 1,
                        path
                    )
                    path.pop()

            else:
                # Letter
                path.append(ch)
                backtrack(
                    index + 1,
                    left,
                    right,
                    balance,
                    path
                )
                path.pop()

        backtrack(0, left_remove, right_remove, 0, [])

        return list(result)








# Optimal:
class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = {s}
        visited = {s}
        result = []

        while queue:
            # Current level = same number of removals
            for string in queue:
                if is_valid(string):
                    result.append(string)

            # If valid strings found, minimum removals achieved
            if result:
                return result

            next_level = set()

            for string in queue:
                for i in range(len(string)):
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.add(new_string)

            queue = next_level

        return [""]