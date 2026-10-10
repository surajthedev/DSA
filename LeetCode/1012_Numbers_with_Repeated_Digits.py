# Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.



# Example 1:

# Input: n = 20
# Output: 1
# Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
# Example 2:

# Input: n = 100
# Output: 10
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
# Example 3:

# Input: n = 1000
# Output: 262


# Constraints:

# 1 <= n <= 109
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
#
#
# ### Brute Force

python
```
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        count = 0

        for num in range(1, n + 1):
            digits = str(num)

            if len(set(digits)) < len(digits):
                count += 1

        return count
```

### Optimal

python
```
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n)))
        length = len(digits)

        def permutation(m, k):
            result = 1
            for i in range(k):
                result *= m - i
            return result

        count = 0

        for length_i in range(1, length):
            count += 9 * permutation(9, length_i - 1)

        used = set()

        for i, digit in enumerate(digits):
            start = 1 if i == 0 else 0

            for d in range(start, digit):
                if d not in used:
                    count += permutation(10 - (i + 1), length - i - 1)

            if digit in used:
                break

            used.add(digit)
        else:
            count += 1

        return n - count
```
