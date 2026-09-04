# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

# The closest is defined as the absolute difference minimized between two integers.

 

# Example 1:

# Input: n = "123"
# Output: "121"
# Example 2:

# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

# Constraints:

# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 1018 - 1].








# Brute force:
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)

        left = num - 1
        right = num + 1

        while True:
            if str(left) == str(left)[::-1]:
                left_diff = num - left
                break
            left -= 1

        while True:
            if str(right) == str(right)[::-1]:
                right_diff = right - num
                break
            right += 1

        if left_diff <= right_diff:
            return str(left)

        return str(right)










# Optimal:
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)

        candidates = set()

        candidates.add(10 ** (length - 1) - 1)
        candidates.add(10 ** length + 1)

        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        for x in [prefix - 1, prefix, prefix + 1]:
            s = str(x)

            if length % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]

            candidates.add(int(pal))

        candidates.discard(num)

        return str(min(candidates, key=lambda x: (abs(x - num), x)))