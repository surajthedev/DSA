# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.



# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false


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
# Brute force:
from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)

        for p in set(permutations(s)):
            if p[0] == '0':
                continue

            num = int(''.join(p))

            if num > 0 and (num & (num - 1)) == 0:
                return True

        return False






# Optimal:
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = sorted(str(n))

        power = 1

        while power <= 10**9:
            if sorted(str(power)) == target:
                return True
            power *= 2

        return False
