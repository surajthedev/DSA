# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.

# Return the minimum number of insertions needed to make s balanced.



# Example 1:

# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
# Example 2:

# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
# Example 3:

# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.


# Constraints:

# 1 <= s.length <= 105
# s consists of '(' and ')' only.
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
# ### Brute Force

python
```

class Solution:
    def minInsertions(self, s: str) -> int:
        s = list(s)
        insertions = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                if i + 1 < len(s) and s[i + 1] == ')':
                    if i + 2 < len(s) and s[i + 2] == ')':
                        i += 3
                    else:
                        s.insert(i + 2, ')')
                        insertions += 1
                        i += 3
                else:
                    s.insert(i + 1, ')')
                    s.insert(i + 1, ')')
                    insertions += 2
                    i += 3
            else:
                s.insert(i, '(')
                insertions += 1
                i += 3

        return insertions
```

### Optimal — O(n) Time, O(1) Space

python
```

class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_count += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    insertions += 1

            i += 1

        return insertions + 2 * open_count
```
