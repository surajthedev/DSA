# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9


# Brute Force Approach:

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def isSequential(num):
            s = str(num)

            for i in range(1, len(s)):
                if int(s[i]) != int(s[i - 1]) + 1:
                    return False

            return True

        ans = []

        for num in range(low, high + 1):
            if isSequential(num):
                ans.append(num)

        return ans


# Optimized Approach:
# Idea
# Sequential digits can only be formed from the string "123456789".
# Examples:
# 123
# 234
# 345
# 456
# 567
# 678
# 789
# For 4-digit numbers:
# 1234
# 2345
# 3456
# 4567
# 5678
# 6789
# So instead of checking every number between low and high, we generate all possible sequential digit numbers by taking substrings from "123456789".
# Then, we check which generated numbers lie within the range [low, high] and add them to the answer list.
# Code

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        digits = "123456789"
        ans = []

        minLen = len(str(low))
        maxLen = len(str(high))

        for length in range(minLen, maxLen + 1):

            for start in range(10 - length):

                num = int(digits[start:start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans

# Time Complexity
# O(1)
# There are only a limited number of possible sequential digit numbers.
# At maximum, we generate only 36 numbers (for lengths from 2 to 9), so the runtime remains constant.
# Space Complexity
# O(1)