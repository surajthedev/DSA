# Given a string formula representing a chemical formula, return the count of each atom.

# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.

# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.

# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

# Example 1:

# Input: formula = "H2O"
# Output: "H2O"
# Explanation: The count of elements are {'H': 2, 'O': 1}.
# Example 2:

# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:

# Input: formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

# Constraints:

# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.














# Brute Force
from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)

        def parse(start):
            count = Counter()
            i = start

            while i < n and formula[i] != ')':
                if formula[i] == '(':
                    sub, i = parse(i + 1)
                    i += 1

                    j = i
                    while j < n and formula[j].isdigit():
                        j += 1

                    multiplier = int(formula[i:j]) if i < j else 1

                    for atom, freq in sub.items():
                        count[atom] += freq * multiplier

                    i = j

                else:
                    j = i + 1

                    while j < n and formula[j].islower():
                        j += 1

                    atom = formula[i:j]

                    k = j
                    while k < n and formula[k].isdigit():
                        k += 1

                    multiplier = int(formula[j:k]) if j < k else 1
                    count[atom] += multiplier

                    i = k

            return count, i

        count, _ = parse(0)

        result = []

        for atom in sorted(count):
            result.append(atom)
            if count[atom] > 1:
                result.append(str(count[atom]))

        return "".join(result)
















# Optimal - Stack
from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1

            elif formula[i] == ')':
                i += 1

                j = i
                while j < n and formula[j].isdigit():
                    j += 1

                multiplier = int(formula[i:j]) if i < j else 1
                i = j

                current = stack.pop()

                for atom, count in current.items():
                    stack[-1][atom] += count * multiplier

            else:
                j = i + 1

                while j < n and formula[j].islower():
                    j += 1

                atom = formula[i:j]

                k = j
                while k < n and formula[k].isdigit():
                    k += 1

                count = int(formula[j:k]) if j < k else 1

                stack[-1][atom] += count
                i = k

        result = []

        for atom in sorted(stack[-1]):
            result.append(atom)

            if stack[-1][atom] > 1:
                result.append(str(stack[-1][atom]))

        return "".join(result)
