# You are given a string expression representing a Lisp-like expression to return the integer value of.

# The syntax for these expressions is given as follows.

# An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
# (An integer could be positive or negative.)
# A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
# An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
# A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
# For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
# Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.
 

# Example 1:

# Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
# Output: 14
# Explanation: In the expression (add x y), when checking for the value of the variable x,
# we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
# Since x = 3 is found first, the value of x is 3.
# Example 2:

# Input: expression = "(let x 3 x 2 x)"
# Output: 2
# Explanation: Assignment in let statements is processed sequentially.
# Example 3:

# Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
# Output: 5
# Explanation: The first (add x y) evaluates as 3, and is assigned to x.
# The second (add x y) evaluates as 3+2 = 5.
 

# Constraints:

# 1 <= expression.length <= 2000
# There are no leading or trailing spaces in expression.
# All tokens are separated by a single space in expression.
# The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
# The expression is guaranteed to be legal and evaluate to an integer.












# Solution:
class Solution:
    def evaluate(self, expression: str) -> int:

        def parse(i, scope):
            if expression[i] != '(':
                j = i

                while j < len(expression) and expression[j] not in ' ()':
                    j += 1

                token = expression[i:j]

                if token[0].isdigit() or token[0] == '-':
                    return int(token), j

                return scope[token], j

            i += 1

            # Read operation
            j = i
            while expression[j] not in ' ()':
                j += 1

            op = expression[i:j]
            i = j + 1

            if op == 'add':
                a, i = parse(i, scope)
                i += 1
                b, i = parse(i, scope)
                return a + b, i + 1

            if op == 'mult':
                a, i = parse(i, scope)
                i += 1
                b, i = parse(i, scope)
                return a * b, i + 1

            # let
            new_scope = scope.copy()

            while True:
                # Skip spaces
                while expression[i] == ' ':
                    i += 1

                # Last expression
                if expression[i] == '(':
                    value, next_i = parse(i, new_scope)

                    while expression[next_i] == ' ':
                        next_i += 1

                    if expression[next_i] == ')':
                        return value, next_i + 1

                    i = next_i
                    continue

                # Read token
                j = i
                while expression[j] not in ' ()':
                    j += 1

                token = expression[i:j]

                # If this is the final variable/value
                if expression[j] == ')':
                    if token[0].isdigit() or token[0] == '-':
                        return int(token), j + 1
                    return new_scope[token], j + 1

                # Variable assignment
                i = j + 1

                value, i = parse(i, new_scope)

                new_scope[token] = value

                while expression[i] == ' ':
                    i += 1

                if expression[i] == ')':
                    return value, i + 1

        return parse(0, {})[0]