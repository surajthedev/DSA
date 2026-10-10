# Given an integer n, return a binary string representing its representation in base -2.

# Note that the returned string should not have leading zeros unless the string is "0".



# Example 1:

# Input: n = 2
# Output: "110"
# Explantion: (-2)2 + (-2)1 = 2
# Example 2:

# Input: n = 3
# Output: "111"
# Explantion: (-2)2 + (-2)1 + (-2)0 = 3
# Example 3:

# Input: n = 4
# Output: "100"
# Explantion: (-2)2 = 4


# Constraints:

# 0 <= n <= 109
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
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        result = ""

        while n != 0:
            remainder = n % -2
            n //= -2

            if remainder < 0:
                remainder += 2
                n += 1

            result = str(remainder) + result

        return result
```

### Optimal

python
```
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        result = []

        while n:
            remainder = n & 1
            result.append(str(remainder))
            n = (n - remainder) // -2

        return "".join(result[::-1])
```
