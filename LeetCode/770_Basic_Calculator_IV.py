# Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified expression, such as ["-1*a","14"]

# An expression alternates chunks and symbols, with a space separating each chunk and symbol.
# A chunk is either an expression in parentheses, a variable, or a non-negative integer.
# A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like "2x" or "-x".
# Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

# For example, expression = "1 + 2 * 3" has an answer of ["7"].
# The format of the output is as follows:

# For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
# For example, we would never write a term like "b*a*c", only "a*b*c".
# Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
# For example, "a*a*b*c" has degree 4.
# The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
# An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"].
# Terms (including constant terms) with coefficient 0 are not included.
# For example, an expression of "0" has an output of [].
# Note: You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

 

# Example 1:

# Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
# Output: ["-1*a","14"]
# Example 2:

# Input: expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
# Output: ["-1*pressure","5"]
# Example 3:

# Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
# Output: ["1*e*e","-64"]
 

# Constraints:

# 1 <= expression.length <= 250
# expression consists of lowercase English letters, digits, '+', '-', '*', '(', ')', ' '.
# expression does not contain any leading or trailing spaces.
# All the tokens in expression are separated by a single space.
# 0 <= evalvars.length <= 100
# 1 <= evalvars[i].length <= 20
# evalvars[i] consists of lowercase English letters.
# evalints.length == evalvars.length
# -100 <= evalints[i] <= 100









# Brute Force

from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        values = dict(zip(evalvars, evalints))
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()

        def add(a, b, sign=1):
            res = defaultdict(int)
            for k, v in a.items():
                res[k] += v
            for k, v in b.items():
                res[k] += sign * v
            return {k: v for k, v in res.items() if v}

        def multiply(a, b):
            res = defaultdict(int)

            for x, cx in a.items():
                for y, cy in b.items():
                    vars_ = tuple(sorted(x + y))
                    res[vars_] += cx * cy

            return {k: v for k, v in res.items() if v}

        def parse(i):
            result = {(): 0}

            while i < len(tokens) and tokens[i] != ")":
                sign = 1

                if tokens[i] == "+":
                    i += 1
                elif tokens[i] == "-":
                    sign = -1
                    i += 1

                if tokens[i] == "(":
                    left, i = parse(i + 1)
                    i += 1
                else:
                    t = tokens[i]
                    i += 1

                    if t.isdigit():
                        left = {(): int(t)}
                    elif t in values:
                        left = {(): values[t]}
                    else:
                        left = {(t,): 1}

                while i < len(tokens) and tokens[i] == "*":
                    i += 1

                    if tokens[i] == "(":
                        right, i = parse(i + 1)
                        i += 1
                    else:
                        t = tokens[i]
                        i += 1

                        if t.isdigit():
                            right = {(): int(t)}
                        elif t in values:
                            right = {(): values[t]}
                        else:
                            right = {(t,): 1}

                    left = multiply(left, right)

                result = add(result, left, sign)

            return result, i

        poly, _ = parse(0)

        terms = [
            (vars_, coef)
            for vars_, coef in poly.items()
            if coef != 0
        ]

        terms.sort(key=lambda x: (-len(x[0]), x[0]))

        ans = []

        for vars_, coef in terms:
            if vars_:
                ans.append(str(coef) + "*" + "*".join(vars_))
            else:
                ans.append(str(coef))

        return ans

















# Optimal

from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        values = dict(zip(evalvars, evalints))
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
        pos = 0

        def add(a, b, sign=1):
            res = defaultdict(int, a)

            for k, v in b.items():
                res[k] += sign * v

            return {k: v for k, v in res.items() if v}

        def mul(a, b):
            res = defaultdict(int)

            for x, cx in a.items():
                for y, cy in b.items():
                    key = tuple(sorted(x + y))
                    res[key] += cx * cy

            return {k: v for k, v in res.items() if v}

        def parse():
            nonlocal pos

            result = {}
            sign = 1

            while pos < len(tokens) and tokens[pos] != ")":
                if tokens[pos] == "+":
                    sign = 1
                    pos += 1
                elif tokens[pos] == "-":
                    sign = -1
                    pos += 1

                if tokens[pos] == "(":
                    pos += 1
                    cur = parse()
                    pos += 1
                else:
                    token = tokens[pos]
                    pos += 1

                    if token.isdigit():
                        cur = {(): int(token)}
                    elif token in values:
                        cur = {(): values[token]}
                    else:
                        cur = {(token,): 1}

                while pos < len(tokens) and tokens[pos] == "*":
                    pos += 1

                    if tokens[pos] == "(":
                        pos += 1
                        nxt = parse()
                        pos += 1
                    else:
                        token = tokens[pos]
                        pos += 1

                        if token.isdigit():
                            nxt = {(): int(token)}
                        elif token in values:
                            nxt = {(): values[token]}
                        else:
                            nxt = {(token,): 1}

                    cur = mul(cur, nxt)

                result = add(result, cur, sign)

            return result

        poly = parse()

        items = [(k, v) for k, v in poly.items() if v]

        items.sort(key=lambda x: (-len(x[0]), x[0]))

        ans = []

        for vars_, coef in items:
            if vars_:
                ans.append(f"{coef}*" + "*".join(vars_))
            else:
                ans.append(str(coef))

        return ans