# Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

# Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].



# Example 1:

# Input: left = "4", right = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
# Example 2:

# Input: left = "1", right = "2"
# Output: 1


# Constraints:

# 1 <= left.length, right.length <= 18
# left and right consist of only digits.
# left and right cannot have leading zeros.
# left and right represent integers in the range [1, 1018 - 1].
# left is less than or equal to right.









# Brute force:
import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        l = int(left)
        r = int(right)
        ans = 0

        for num in range(l, r + 1):
            s = str(num)

            if s != s[::-1]:
                continue

            root = math.isqrt(num)

            if root * root == num:
                rs = str(root)
                if rs == rs[::-1]:
                    ans += 1

        return ans










# Optimal:
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)

        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]

        ans = 0

        # sqrt(10^18) = 10^9
        # Generate palindromic roots up to 10^9.
        for half in range(1, 100000):
            s = str(half)

            # Odd-length palindrome
            root = int(s + s[-2::-1])
            square = root * root

            if square > R:
                break

            if square >= L and is_palindrome(square):
                ans += 1

            # Even-length palindrome
            root = int(s + s[::-1])
            square = root * root

            if L <= square <= R and is_palindrome(square):
                ans += 1

        # Root = 1 is already covered.
        return ans
