# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

# Note that operands in the returned expressions should not contain leading zeros.

# Note that a number can contain multiple digits.

 

# Example 1:

# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
# Example 3:

# Input: num = "3456237490", target = 9191
# Output: []
# Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 

# Constraints:

# 1 <= num.length <= 10
# num consists of only digits.
# -231 <= target <= 231 - 1





# Brute force:
class Solution:
    def addOperators(self, num, target):
        result = []

        def evaluate(expr):
            # Python eval se expression calculate kar sakte hain
            return eval(expr)

        def backtrack(index, expression):
            if index == len(num):
                if evaluate(expression) == target:
                    result.append(expression)
                return

            for end in range(index + 1, len(num) + 1):

                # Leading zero avoid karo
                if end > index + 1 and num[index] == '0':
                    break

                current = num[index:end]

                if index == 0:
                    backtrack(end, current)
                else:
                    backtrack(end, expression + "+" + current)
                    backtrack(end, expression + "-" + current)
                    backtrack(end, expression + "*" + current)

        backtrack(0, "")

        return result







# Optimal:
class Solution:
    def addOperators(self, num, target):
        result = []

        def backtrack(index, expression, value, last):
            # Entire string use ho gayi
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for end in range(index + 1, len(num) + 1):

                # Leading zero allowed nahi
                if end > index + 1 and num[index] == '0':
                    break

                current_str = num[index:end]
                current = int(current_str)

                # First number
                if index == 0:
                    backtrack(
                        end,
                        current_str,
                        current,
                        current
                    )

                else:
                    # +
                    backtrack(
                        end,
                        expression + "+" + current_str,
                        value + current,
                        current
                    )

                    # -
                    backtrack(
                        end,
                        expression + "-" + current_str,
                        value - current,
                        -current
                    )

                    # *
                    backtrack(
                        end,
                        expression + "*" + current_str,
                        value - last + last * current,
                        last * current
                    )

        backtrack(0, "", 0, 0)

        return result